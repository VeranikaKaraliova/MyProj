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
    cart, create = models.Cart.objects.get_or_create(
        pk = cart_pk,
        defaults={'user' : user,}
    )
    
    return cart, create

class AddBookInCart(UpdateView):
    models = models.BookInCart
    template_name = 'cart/add.html'
    fields = ['quantity']
    success_url = reverse_lazy('bookapp:list')
    def get_object(self, *args, **kwargs):
        #cart_pk = self.request.session.get('cart_id', 0)
        bookapp_pk = self.request.GET.get('bookapp_pk')
        bookapp = BookApp.objects.get(pk=int(bookapp_pk))
        cart, create = get_cart(self.request)
        if create:
            self.request.session['cart_pk'] = cart.pk
        obj, create = self.models.objects.get_or_create(
            cart = cart,
            book = bookapp,
            defaults={}
        )
        return obj

class CartDatail(DetailView):
    model = models.Cart
    template_name = 'cart/cart.html'
    def get_object(self):
        cart = get_cart(self.request)
        cart, create  = get_cart(self.request)
        if create :
            self.request.session['cart_pk'] = cart.pk
        return cart

class BookInCartDelete(DeleteView):
    model = models.BookInCart
    template_name = "cart/delete.html"
    success_url = reverse_lazy('cart:cart')