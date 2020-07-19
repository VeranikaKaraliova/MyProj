from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from book.models import BookApp

from django.urls import reverse_lazy
from . import models

def get_cart(request):
    cart_pk = request.session.get('cart_pk')
    user = request.user
    if user.is_anonymous:
        user = None
    if cart_pk is not None:
        cart_pk=int(cart_pk)
    cart, created = models.Cart.objects.get_or_create(
        pk = cart_pk,
        defaults={'user' : user,}
    )
    
    return cart, created

class AddBookInCart(UpdateView):
    model = models.BookInCart
    template_name = 'cart/add.html'
    fields = ['quantity']
    success_url = '/book/list-bookapp/'
    def get_object(self):
        #cart_pk = self.request.session.get('cart_id', 0)
        bookapp_pk = self.request.GET.get('bookapp_pk')
        bookapp = BookApp.objects.get(pk=int(bookapp_pk))
        cart, created = get_cart(self.request)
        if created:
            self.request.session['cart_pk'] = cart.pk
        obj, created = self.model.objects.get_or_create(
            cart = cart,
            book = bookapp,
            defaults={}
        )
        return cart

class CartDatail(DetailView):
    model = models.Cart
    template_name = 'cart/cart.html'
    def get_object(self):
        cart = get_cart(self.request)
        cart, created  = get_cart(self.request)
        if created :
            self.request.session['cart_pk'] = cart.pk
        return cart