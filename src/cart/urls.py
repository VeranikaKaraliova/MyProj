from django.urls import path
from . import views
app_name = "cart"

urlpatterns = [
    path('add/', views.AddBookInCart.as_view(), name="add"),
    path('cart/', views.CartDatail.as_view(), name="cart"),
]