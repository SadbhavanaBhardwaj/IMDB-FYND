from django.shortcuts import render

# Create your views here.

from users.models import ImdbUser
from movies.models import Genre, Movie, Rating
from movies.serializers import RatingSerializer, MovieSerializer, MovieListSerializer
from users.permissions import IsAdmin
from movies.pagination import MoviesPagination


from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status

class MovieListAPIView(ListAPIView):
    serializer_class = MovieListSerializer
    queryset = Movie.objects.all()
    pagination_class = MoviesPagination

    def get_queryset(self, *args, **kwargs):
        """
            returns queryset of Movie which contains the string provided in the name param of URL
        """
        name = self.request.GET.get('name', None)
        qs = Movie.objects.all()
        if name:
            qs = qs.filter(name__icontains=name)
        return qs


class MovieRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = (IsAdmin, )

    def get(self, request, pk):
        try:
            movie = Movie.objects.get(id=pk)
        except Exception as e:
            return Response({"msg": str(e)})
        movie_serializer = MovieListSerializer(movie).data
        return Response(movie_serializer, status=status.HTTP_200_OK)

class MovieCreateAPIView(CreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = (IsAdmin, )
    #201 done



#testing nhi ho pa rhi pta nhi kyu!!
class RateMovieCreateAPIView(CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated, )
    # 200, 401, 
    def post(self, request, pk):
        print(request.data)
        data = request.data
        user = request.META.get('HTTP_AUTHORIZATION')
        user_id = Token.objects.get(key=user.split(" ")[1]).user.id
        data['movie'] = pk
        data['user'] = user_id
        rating = RatingSerializer(data=data)
        print(rating.is_valid())
        if rating.is_valid():
            rating.save()
        else:
            return Response(rating.errors)
        return Response(rating.data)



