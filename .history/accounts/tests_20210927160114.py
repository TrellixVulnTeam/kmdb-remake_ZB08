from rest_framework.test import APITestCase, APIClient
class AccountTest(APITestCase):
    client = APIClient()

    def setUp(self) -> None:
        self.superuser_resgistration_data = {
            "username":"user",
            "password":"1234",
            "first_name":"John",
            "last_name":"Wick",
            "is_superuser":True,
            "is_staff":True,
        }
        

