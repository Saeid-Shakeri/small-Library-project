from django.urls import path
from . import views


urlpatterns = [
    path("all/", views.list, name="home"),

    path("<int:book_id>/", views.book_detail, name="book_detail"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
    path("author/<int:author_id>/books/", views.author_books_list, name="author_books_list"),

]