from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from book.models import BookApp

from . import models

class AddBookInCart(UpdateView):
    model = models.BookInCart
    template_name = 'cart/add.html'
    fields = ['quantity',]

    def get_object(self):
        cart_pk = self.request.session.get('cart_id', 0)
        bookapp_pk = self.request.GET.get('bookapp_pk')
        bookapp = BookApp.objects.get(pk = bookapp_pk)
        user = self.request.user
        #self.models.objects.get(pk=self.kwargs.get('pk'))
        #self.kwargs.get('vas')
        cart, create = models.Cart.objects.get_or_create(
            pk = int(cart_pk),
            user = user,
            defaults={}
        )
        if create:
            self.request.session['cart_pk'] = cart.pk
        obj, create = self.model.objects.get_or_create(
            cart = cart,
            book = bookapp,
            defaults={}
        )
        return obj
