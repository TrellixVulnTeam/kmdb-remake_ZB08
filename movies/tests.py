from rest_framework.test import APITestCase, APIClient
import ipdb

class MoviesTest(APITestCase):
    client = APIClient()

    def test_created_movie_success(self):
        superuser_sign_in_data = {
            "username":"user",
            "password":"1234",
            "first_name":"John",
            "last_name":"Wick",
            "is_superuser":True,
            "is_staff":True,
        }
        self.client.post('/api/accounts/', superuser_sign_in_data, format='json')

        superuser_sign_up_data = {
            "username":"user",
            "password":"1234",
        }
        self.client.post('/api/login/', superuser_sign_up_data, format='json')

        movie_data = {
            "title": "O Poderoso Chefão 2",
            "duration": "175m",
            "genres": [
                {"name": "Crime"},
                {"name": "Drama"}
            ],
            "premiere": "1972-09-10",
            "classification": 14,
            "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' ..."
        }
        movie_response_data = {
            "id": 1,
            "title": "O Poderoso Chefão 2",
            "duration": "175m",
            "genres": [
                {
                    "id": 1,
                    "name": "Crime"
                },
                {
                    "id": 2,
                    "name": "Drama"
                }
            ],
            "premiere": "1972-09-10",
            "classification": 14,
            "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' ..."
        }

        response = self.client.post('/api/movies/', movie_data, format='json')
        self.assertDictContainsSubset(movie_response_data, response.json())
