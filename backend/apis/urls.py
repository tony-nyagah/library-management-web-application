from django.urls import path

from apis.views import BookAPIView

urlpatterns = [path("books/", BookAPIView.as_view(), name="book_list")]
