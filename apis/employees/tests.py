from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from authentication.models import BaseUser
from apis.companies.models import Company
from apis.departments.models import Department
from apis.employees.models import Employee


class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        # Create a superuser for authentication
        self.superuser = BaseUser.objects.create_superuser(
            email="admin@admin.com",
            password="admin"
        )

        # Get the JWT auth token
        response = self.client.post(reverse('authentication:token_obtain_pair'), {
            'email': 'admin@admin.com',
            'password': 'admin'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Create a test company
        self.company = Company.objects.create(
            name="Test Company",
            cnpj="00.000.000/0000-00",
            address="Test Address",
            country="Test Country"
        )

        # Create a test department
        self.department = Department.objects.create(
            name="HR",
            cost_center="123",
            integration_code="HR123",
            company=self.company
        )

        # Create a test employee
        self.employee = Employee.objects.create(
            full_name="Generic Employee",
            email="generic@example.com",
            phone_number="1234567890",
            birthdate="1990-01-01",
            admission_date="2020-01-01",
            department=self.department,
            city="Generic City"
        )

    def test_create_employee(self):
        """
        Test creating a new employee.
        """
        url = reverse('employees:employee-list')
        data = {
            "full_name": "John Doe",
            "email": "john.doe@example.com",
            "phone_number": "1234567890",
            "birthdate": "1990-01-01",
            "admission_date": "2020-01-01",
            "department": self.department.id,
            "city": "New York"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)
        self.assertEqual(Employee.objects.get(email="john.doe@example.com").full_name, 'John Doe')

    def test_list_employees(self):
        """
        Test listing all employees.
        """
        url = reverse('employees:employee-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        """
        Test updating an employee.
        """
        url = reverse('employees:employee-detail', kwargs={'pk': self.employee.id})
        data = {
            "full_name": "Updated Name",
            "email": "final@example.com",
            "phone_number": "1234567890",
            "birthdate": "1985-01-02",
            "admission_date": "2019-01-02",
            "department": self.department.id,
            "city": "Updated City"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.full_name, 'Updated Name')
        self.assertEqual(self.employee.city, 'Updated City')

    def test_partial_update_employee(self):
        """
        Test partially updating an employee.
        """
        url = reverse('employees:employee-detail', kwargs={'pk': self.employee.id})
        data = {"city": "Partially Updated City"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.city, 'Partially Updated City')

    def test_get_employee(self):
        """
        Test retrieving a specific employee.
        """
        url = reverse('employees:employee-detail', kwargs={'pk': self.employee.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        """
        Test deleting (setting inactive) an employee.
        """
        url = reverse('employees:employee-detail', kwargs={'pk': self.employee.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.employee.refresh_from_db()
        self.assertFalse(self.employee.is_active)
