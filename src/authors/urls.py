from django.urls import path
from . import views
app_name = "authors"

urlpatterns = [
    path('create-authors/', views.CreateAuthors.as_view(), name="create"),
    path('update-authors/<int:pk>', views.UpdateAuthors.as_view(), name="update"),
    path('list-authors/', views.ListAuthors.as_view(), name="list"),
    path('delete-authors/<int:pk>', views.DeleteAuthors.as_view(), name="delete"),
    path('authors-books/<int:pk>', views.AuthorsBooks.as_view(), name="books"),
]