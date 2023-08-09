from rest_framework import serializers

from catalog.models import Book, Author, Genre, Language


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = (
            "url",
            "id",
            "title",
            "author",
            "summary",
            "isbn",
            "genre",
            "language",
        )
        # depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
            "date_of_death",
        )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            "id",
            "name",
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
        )
