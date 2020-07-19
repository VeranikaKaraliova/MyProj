"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from testapp.views import test
from testgenre.views import CreateGenre, UpdateGenre, ListGenre, DeleteGenre
from django.conf import settings
from django.conf.urls.static import static
#from profiles.auth import MyLogin, MyLogout
from book.views import HomePage
#from testgenre import urls as testgenre_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-genre/', CreateGenre.as_view(), name='create-genre'),
    #path('update-genre/<int:pk>', UpdateGenre.as_view(), name='update'),
    path('', HomePage.as_view(), name='home-page'),
    #path('delete-genre/<int:pk>', DeleteGenre.as_view(), name='delete'),
    path('testgenre/', include('testgenre.urls', namespace='genres')),
    path('authors/', include('authors.urls', namespace='authors')),
    path('publisher/', include('publisher.urls', namespace='publisher')),
    path('book/', include('book.urls', namespace='bookapp')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('checkout/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    #path('login/', MyLogin.as_view(), name='login'),
    #path('logout/', MyLogout.as_view(), name='logout'),

    #path('profiles/', include('django.contrib.auth.urls')), # для авторизации 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

