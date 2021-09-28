from rest_framework.test import APITestCase, APIClient
class AccountTest(APITestCase):
    client = APIClient()

    def test_created_superuser_success(self):
        superuser_sign_in_data = {
            "username":"user",
            "password":"1234",
            "first_name":"John",
            "last_name":"Wick",
            "is_superuser":True,
            "is_staff":True,
        }
        superuser_response_data = {
            "id": 1,
            "username":"user",
            "first_name":"John",
            "last_name":"Wick",
            "is_superuser":True,
            "is_staff":True,
        }

        response = self.client.post('/api/accounts/', superuser_sign_in_data, format='json')

        self.assertDictContainsSubset(superuser_response_data, response.json())

    def test_created_superuser_error(self):
        superuser_sign_in_data = {
            "password":"1234",
            "first_name":"John",
            "last_name":"Wick",
            "is_staff":True,
        }

        response = self.client.post('/api/accounts/', )
