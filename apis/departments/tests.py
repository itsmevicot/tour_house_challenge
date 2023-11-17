from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apis.companies.models import Company
from apis.departments.models import Department
from authentication.models import BaseUser


class DepartmentAPITestCase(APITestCase):
    def setUp(self):
        # Create a superuser for authentication
        self.superuser = BaseUser.objects.create_superuser(
            email="admin@admin.com", password="admin"
        )
        # Get the JWT auth token
        response = self.client.post(reverse('authentication:token_obtain_pair'), {
            'email': 'admin@admin.com', 'password': 'admin'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Create a test company
        self.company = Company.objects.create(
            name="Test Company",
            cnpj="61.658.755/0001-72",
            address="Test Address",
            country="Test Country"
        )
        # Create a test department
        self.department = Department.objects.create(
            name="Sales",
            cost_center="CC123",
            integration_code="SL123",
            company=self.company
        )

    def test_create_department(self):
        """
        Test creating a new department.
        """
        url = reverse('departments:department-list')
        data = {
            "name": "HR",
            "cost_center": "CC456",
            "integration_code": "IC456",
            "company": self.company.id
        }
        response = self.client.post(url, data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 2)
        self.assertEqual(Department.objects.get(integration_code="IC456").integration_code, "IC456")

    def test_list_departments(self):
        """
        Test listing all departments.
        """
        url = reverse('departments:department-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        self.assertTrue(any(dept['name'] == "Sales" for dept in results))

    def test_get_department(self):
        """
        Test retrieving a specific department by ID.
        """
        url = reverse('departments:department-detail', kwargs={'pk': self.department.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.department.name)

    def test_update_department(self):
        """
        Test updating a specific department by ID.
        """
        url = reverse('departments:department-detail', kwargs={'pk': self.department.id})
        data = {
            "name": "HR Updated",
            "cost_center": "1234",
            "integration_code": "HR1234",
            "company": self.company.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.department.refresh_from_db()
        self.assertEqual(self.department.name, 'HR Updated')
        self.assertEqual(self.department.cost_center, '1234')

    def test_partial_update_department(self):
        """
        Test partially updating a specific department by ID.
        """
        url = reverse('departments:department-detail', kwargs={'pk': self.department.id})
        data = {"name": "HR Partially Updated"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.department.refresh_from_db()
        self.assertEqual(self.department.name, 'HR Partially Updated')

    def test_delete_department(self):
        """
         Test deleting (inactivating) a specific department by ID.
         """
        url = reverse('departments:department-detail', kwargs={'pk': self.department.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.department.refresh_from_db()
        self.assertFalse(self.department.is_active)

