from rest_framework import serializers

from catalog.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "summary", "isbn", "genre", "language")
