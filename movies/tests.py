from django.test import TestCase
from django.contrib.auth.models import Group
# Create your tests here.

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
import pytest, pytz
from rest_framework.authtoken.models import Token
from movies.models import Movie, Rating, Genre
from users.models import ImdbUser
import json 

@pytest.mark.django_db
class MovieUpdatePIViewTest(APITestCase):
    def setUp(self):

        Group.objects.create(name="ADMIN")
        user = ImdbUser.objects.create(
            email="bhardwajishoo@gmail.com",
            password="admin",
            first_name="ishoo",
            last_name="bhardwaj"
        )
        #user.groups.add(1)
        Genre.objects.create(name="Comedy")

        #movie creation for testing the Rate API
        m = Movie.objects.create(
            name = "Border",
            director = "Director1",
            popularity = 99.9,
        )
        m.genre.add(1)
        token, created = Token.objects.get_or_create(user=user)


    def test_api_view_movie_update(self):
        data = {
            "name": 1,
            "director":"Directr1",
            "popularity":99.9,
            "genre": [1]
        }
        movie = Movie.objects.first().id
        url = "http://127.0.0.1:8000/api/movies/movie/"+str(movie)+"/"
        user = ImdbUser.objects.first()
        token = Token.objects.get(user=user)
        print(token.user)
        token = token.key
        response = self.client.put(url, data, headers={"HTTP_AUTHORIZATION": "Token "+token}, format='json')
        print(response.content)
        self.assertEqual(response.status_code, 200)



@pytest.mark.django_db
class MovieCreateAPIViewTest(APITestCase):

    def setUp(self):

        Group.objects.create(name="ADMIN")
        user = ImdbUser.objects.create(
            email="bhardwajihoo@gmail.com",
            password="admin",
            first_name="ishoo",
            last_name="bhardwaj"
        )
        user.groups.add(1)
        Genre.objects.create(name="Comedy")

        #movie creation for testing the Rate API
        m = Movie.objects.create(
            name = "Border",
            director = "Director1",
            popularity = 99.9,
        )
        m.genre.add(1)
        token, created = Token.objects.get_or_create(user=user)


    def test_api_view_movie_post_success(self):    
        data = {
            "name": "Welcome",
            "director": "pta nhi",
            "popularity": 98.8, 
            "genre": [1]
        }

        url = "http://127.0.0.1:8000/api/movies/create_movie/"
        token = Token.objects.first()
        print(token.user)
        token = token.key
        response = self.client.post(url, data, format='json', headers={"HTTP_AUTHORIZATION": "Token "+token})
        self.assertEqual(response.status_code, 201)

    def test_api_view_movie_post_success(self):    
        data = {
            "name": "Welcome",
            "director": "pta nhi",
            "popularity": 98.8, 
            "genre": [1]
        }

        url = "http://127.0.0.1:8000/api/movies/create_movie/"
        token = Token.objects.first().key

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)
        
    


@pytest.mark.django_db
class MovieRateAPIViewTest(APITestCase):
    def setUp(self):

        Group.objects.create(name="ADMIN")
        user = ImdbUser.objects.create(
            email="bhardwajishoo@gmail.com",
            password="admin",
            first_name="ishoo",
            last_name="bhardwaj"
        )
        #user.groups.add(1)
        Genre.objects.create(name="Comedy")

        #movie creation for testing the Rate API
        m = Movie.objects.create(
            name = "Border",
            director = "Director1",
            popularity = 99.9,
        )
        m.genre.add(1)
        token, created = Token.objects.get_or_create(user=user)


    def test_api_view_movie_rate(self):
        data = {
            "score": 8
        }
        movie = Movie.objects.first().id
        url = "http://127.0.0.1:8000/api/movies/movie/"+str(movie)+"/rate/"
        user = ImdbUser.objects.first()
        token = Token.objects.get(user=user).key
        response = self.client.post(url, data, headers={"HTTP_AUTHORIZATION": "Token "+token}, format='json')
        print(response.content)
        self.assertEqual(response.status_code, 200)



