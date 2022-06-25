from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from hequavur.apps.core.views import DepartmentList, DepartmentDetail, FileDetail, CandidateList, CandidateCreate
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView


class ApiUrlsTests(SimpleTestCase):

    def test_get_customers_is_resolved(self):
        url = reverse('department')
        self.assertEquals(resolve(url).func.view_class, DepartmentList)


def _create_test_file(file_path):
    f = open(file_path, 'w')
    f.write('test123\n')
    f.close()
    f = open(file_path, 'rb')
    return {'datafile': f}


class CoreAPIViewTests(APITestCase):
    # customers_url = reverse("customer")

    def setUp(self):
        data = {
            "department_name": "IT"
        }
        response = self.client.post(reverse("department"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 2)    # {'id': 1, 'department_name': 'IT'}

    def test_create_candidate(self):
        data = {
            "full_name": "testo",
            "date_of_birth": "2022-06-06",
            "years_of_experience": "3",
            "department": "1",
            "resume": _create_test_file('/tmp/test_upload.pdf')
        }
        response = self.client.post(reverse("candidate-create"), data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 5)


#     def test_get_customers_authenticated(self):
#         response = self.client.get(self.customers_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_customers_un_authenticated(self):
#         self.client.force_authenticate(user=None, token=None)
#         response = self.client.get(self.customers_url)
#         self.assertEquals(response.status_code, 401)
#
#     def test_post_customer_authenticated(self):
#         data = {
#             "title": "Mr",
#             "name": "Peter",
#             "last_name": "Parkerz",
#             "gender": "M",
#             "status": "published"
#         }
#         response = self.client.post(self.customers_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(len(response.data), 8)
#
#
# class CustomerDetailAPIViewTests(APITestCase):
#     customer_url = reverse('customer-detail', args=[1])
#     customers_url = reverse("customer")
#
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='admin', password='admin')
#         self.token = Token.objects.create(user=self.user)
#         #self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
#
#         # Saving customer
#         data = {
#             "title": "Mrs",
#             "name": "Johnson",
#             "last_name": "MOrisee",
#             "gender": "F",
#             "status": "published"
#         }
#         self.client.post(
#             self.customers_url, data, format='json')
#
#     def test_get_customer_autheticated(self):
#         response = self.client.get(self.customer_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['name'], 'Johnson')
#
#     def test_get_customer_un_authenticated(self):
#         self.client.force_authenticate(user=None, token=None)
#         response = self.client.get(self.customer_url)
#         self.assertEqual(response.status_code, 401)
#
#     def test_delete_customer_authenticated(self):
#         response = self.client.delete(self.customer_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)