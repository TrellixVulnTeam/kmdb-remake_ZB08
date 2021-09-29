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

    def test_show_all_movies(self):
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
        post_movie1 = self.client.post('/api/movies/', movie_data, format='json')

        movie_data2 = {
            "title": "Um Sonho de Liberdade",
            "duration": "142m",
            "genres": [
                {"name": "Drama"},
                {"name": "Ficção científica"}
            ],
            "premiere": "1994-10-14",
            "classification": 16,
            "synopsis": "Andy Dufresne é condenado a duas prisões perpétuas..."
        }
        post_movie2 = self.client.post('/api/movies/', movie_data2, format='json')


        list_movies_response = [
            {
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
            },
            {
                "id": 2,
                "title": "Um Sonho de Liberdade",
                "duration": "142m",
                "genres": [
                    {
                        "id": 2,
                        "name": "Drama"
                    },
                    {
                        "id": 3,
                        "name": "Ficção científica"
                    }
                ],
                "premiere": "1994-10-14",
                "classification": 16,
                "synopsis": "Andy Dufresne é condenado a duas prisões perpétuas..."
            }
        ]
        response = self.client.get('/api/movies/', format='json')
        self.assertEqual(list_movies_response, response.json())

    def test_retrieve_movie_view_success(self):
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
        self.client.post('/api/movies/', movie_data, format='json')

        response_data = {
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
                "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' ...",
        }
        
        response = self.client.get('/api/movies/1/', format='json')
        self.assertEqual(response_data, response.json())
