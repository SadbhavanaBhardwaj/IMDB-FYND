from movies.views import MovieListAPIView, MovieRetrieveUpdateDeleteAPIView, MovieCreateAPIView, RateMovieCreateAPIView

from django.urls import path

urlpatterns = [
    path('get_movies/', MovieListAPIView.as_view()),
    path('movie/<int:pk>/', MovieRetrieveUpdateDeleteAPIView.as_view()),
    path('create_movie/', MovieCreateAPIView.as_view()),
    path('movie/<int:pk>/rate/', RateMovieCreateAPIView.as_view())
]