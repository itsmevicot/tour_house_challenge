from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apis.companies.models import Company
from authentication.models import BaseUser


class CompanyAPITestCase(APITestCase):
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
            cnpj="00.000.000/0000-00",
            address="Test Address",
            country="Test Country"
        )

    def test_create_company(self):
        """
        Test creating a new company.
        """
        url = reverse('companies:company-list')
        data = {
            "name": "New Company",
            "cnpj": "39.242.215/0001-54",
            "address": "New Address",
            "country": "New Country"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 2)
        self.assertEqual(Company.objects.get(cnpj="39242215000154").cnpj, "39242215000154")

    def test_list_companies(self):
        """
        Test listing all companies.
        """
        url = reverse('companies:company-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data)
        self.assertTrue(any(comp['name'] == "Test Company" for comp in results))

    def test_get_company(self):
        """
        Test retrieving a specific company by ID.
        """
        url = reverse('companies:company-detail', kwargs={'pk': self.company.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.company.name)

    def test_update_company(self):
        """
        Test updating a specific company by ID.
        :return:
        """
        url = reverse('companies:company-detail', kwargs={'pk': self.company.id})
        data = {
            "name": "Updated Company",
            "cnpj": "70.064.478/0001-60",
            "address": "Updated Address",
            "country": "Updated Country"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.company.refresh_from_db()
        self.assertEqual(self.company.name, 'Updated Company')

    def test_partial_update_company(self):
        """
        Test partially updating a specific company by ID.
        """
        url = reverse('companies:company-detail', kwargs={'pk': self.company.id})
        data = {"name": "Partially Updated Company"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.company.refresh_from_db()
        self.assertEqual(self.company.name, 'Partially Updated Company')

    def test_delete_company(self):
        """
        Test deleting (inactivating) a specific company by ID.
        """
        company = Company.objects.create(
            name="Original Company",
            cnpj="60.735.776/0001-81",
            address="Original Address",
            country="Original Country"
        )
        url = reverse('companies:company-detail', kwargs={'pk': company.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        company.refresh_from_db()
        self.assertFalse(company.is_active)

