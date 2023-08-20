from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.movies),
    path('movies/<int:movie_id>', views.movie),
    path('books/', views.books),
    path('books/<int:book_id>', views.book),
    # path('movies/<int:arg>', views.movie)
]
