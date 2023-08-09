from django.urls import path

from catalog.views import (
    BookListView,
    BookDetailView,
    AuthorListView,
    AuthorDetailView,
    GenreListView,
    GenreDetailView,
    LanguageDetailView,
    LangugeListView,
)

urlpatterns = [
    path("book/", BookListView.as_view(), name="book-list"),
    path("book/<int:pk>", BookDetailView.as_view(), name="book-detail"),
    path("author/", AuthorListView.as_view(), name="author-list"),
    path("author/<int:pk>", AuthorDetailView.as_view(), name="author-detail"),
    path("genre/", GenreListView.as_view(), name="genre-list"),
    path("genre/<int:pk>", GenreDetailView.as_view(), name="genre-detail"),
    path("language/", LangugeListView.as_view(), name="language-list"),
    path("language/<int:pk>", LanguageDetailView.as_view(), name="language-detail"),
]
