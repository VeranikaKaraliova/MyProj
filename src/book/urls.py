from django.urls import path
from . import views
app_name = "book"

urlpatterns = [
    path('create-bookapp/', views.CreateBookApp.as_view(), name="create"),
    path('update-bookapp/<int:pk>', views.UpdateBookApp.as_view(), name="update"),
    path('list-bookapp/', views.ListBookApp.as_view(), name="list"),
    path('delete-bookapp/<int:pk>', views.DeleteBookApp.as_view(), name="delete"),
    path('home-page', views.HomePage.as_view(), name="home-page"),
    path('detail-bookapp/<int:pk>', views.DetailBookApp.as_view(), name="detail"),
]