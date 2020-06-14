from django.urls import path
from . import views
app_name = "genres"

urlpatterns = [
    path('create-genre/', views.CreateGenre.as_view(), name="create"),
    path('update-genre/<int:pk>', views.UpdateGenre.as_view(), name="update"),
    path('list-genre/', views.ListGenre.as_view(), name="list"),
    path('delete-genre/<int:pk>', views.DeleteGenre.as_view(), name="delete"),
    
]