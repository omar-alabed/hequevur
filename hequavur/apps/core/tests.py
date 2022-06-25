import os
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class CoreAPIViewTests(APITestCase):

    def setUp(self):
        data = {
            "department_name": "IT"
        }
        response = self.client.post(reverse("department"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 2)    # {'id': 1, 'department_name': 'IT'}

    def test_create_candidate(self):
        with open(os.path.dirname(__file__)+'/pdf-file.pdf', 'rb') as file:
            data = {
                "full_name": "testo",
                "date_of_birth": "2022-06-06",
                "years_of_experience": "3",
                "department": "1",
                "resume": file
            }
            response = self.client.post(reverse("candidate-create"), data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(len(response.data), 7)
            # {'id': 1, 'full_name': 'testo', 'date_of_birth': '2022-06-06', 'years_of_experience': 3,
            # 'resume': s3 link,
            # 'create_date': date time now, 'department': 1}

    def test_get_candidates_non_authenticated(self):
        response = self.client.get(reverse("candidate"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_file_non_authenticated(self):
        response = self.client.get(reverse("file-detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
