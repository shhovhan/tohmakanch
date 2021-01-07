from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from bio.models import Biography
from writings.models import Poem, Article, Story, Favourite
from .serializers import BiographySerializer, WritingSerializer, FavouriteSerializer


class BiographyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer

    def list(self, request):
        queryset = Biography.objects.first()
        serializer = BiographySerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = WritingSerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = WritingSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = WritingSerializer


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer