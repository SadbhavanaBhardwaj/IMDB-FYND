**Introduction:**

This service will show the movies list and their meta info like Imdb does.
All the users will be able to see the movies list. Only the authenticated users(admin + registered) will be able to add rating. And the admin can add, update and delete a movie.

---------


If docker and docker-compose are installed in the system, run the below command and directly hit the APIs

1. ```sudo service docker start && docker-compose up -d ```


-----------

Run the below commands before hitting APIs


1. ```pip3 install -r requirements.txt```

2. ```python3 manage.py migrate```

3. Create group "ADMIN" 
    - ```python3 manage.py loaddata scripts/groups.json```

4. Create different Genre:
    - ```python3 manage.py loaddata scripts/genre.json```
        - Note: if you want to add more genre, add them in the scripts/genre.json file 



---------
**APIs**



1. User Registration
    End Point: http://127.0.0.1:8000/api/users/register/
    - POST request:  normal user: request body:
        ```{
            "email": "email@email.com", 
            "password": "pswd", 
            "pswd2": "pswd",    
            "first_name": "first",  
            "last_name": "last",    
            "username": "first_user"    
        }```
    - POST request:  if admin: request body(add group: "ADMIN" in the body): 
        ```{
            "email": "email@email.com",
            "password": "pswd",
            "pswd2": "pswd",
            "first_name": "first",
            "last_name": "last",
            "group": "ADMIN",
            "username": "admin"
        }```

2. Get Authientication Token
    End Point: http://127.0.0.1:8000/api/users/login/ 
    - POST request: request body: 
        ```{
            "username": "first_user",
            "password": "pswd"
        }
        ```

3. Get List of Movies:
    End Point: http://127.0.0.1:8001/api/movies/get_movies/?name="Hera"
    - GET request:  
    - if name is included in the parameters, then the search will include all the movies containing the value of the search param
    - gives paginated reponse. 10 movies per page




4. Add a movie: Only accessible by admin
    End Point: http://127.0.0.1:8000/api/movies/create_movie/
    - POST request: ```{
            "name": "Hera Pheri",
            "popularity": 99.9,
            "director": "Director1",
            "genre": [2]
        }```


5. Update/ Delete a movie (Only admins):
End Point: http://127.0.0.1:8000/api/movies/movie/<int:pk>/
    - PUT request: ```{
        "name": "name1",
        "director": "director1",
        "popularity": 88.9,
        "imdb_score": 8.9,
        "genre": [1, 3]
    }```


    - Delete request:
        send DELETE request to the above EP

6. Rate a movie: Only authenticated users allowed
End Point: http://127.0.0.1:8000/api/movies/movie/<int:pk>/rate/
    - POST request: request body:
        ```{
            "score": 9
        }```