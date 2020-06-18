from django.urls import path
from . import views
app_name = "publisher"

urlpatterns = [
    path('create-publisher/', views.CreatePublisher.as_view(), name="create"),
    path('update-publisher/<int:pk>', views.UpdatePublisher.as_view(), name="update"),
    path('list-publisher/', views.ListPublisher.as_view(), name="list"),
    path('delete-publisher/<int:pk>', views.DeletePublisher.as_view(), name="delete"),
    
]