from catalog.models import Author, Book, Genre, Language
from catalog.serializers import AuthorSerializer, BookSerializer, GenreSerializer
from rest_framework import generics


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class LangugeListView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = GenreSerializer


class LanguageDetailView(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = GenreSerializer
