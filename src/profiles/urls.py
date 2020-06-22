from django.urls import path
from . import views
app_name = "profiles"

urlpatterns = [
    #path('login/',views.ProfilesLogin.as_view(template_name='accounts/login.html'), name='login')
    path('login/', views.ProfilesLogin.as_view(), name='login'),
    #path('create-profiles/', views.CreateAuthors.as_view(), name="create"),
    #path('update-profiles/<int:pk>', views.UpdateAuthors.as_view(), name="update"),
    #path('list-profiles/', views.ListAuthors.as_view(), name="list"),
    #path('delete-profiles/<int:pk>', views.DeleteAuthors.as_view(), name="delete"),
    
]