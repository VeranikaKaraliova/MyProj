from django.views.generic import UpdateView
from cart.models import Cart
from .models import Order
from django.urls import reverse_lazy

class CreateOrder(UpdateView):
    model = Order
    template_name = "order/create.html"
    fields = (
        "delivery_address",
        "contact_phone"
    )
    
    success_url = reverse_lazy('bookapp:home-page')
    def get_object(self):
        cart_id = self.request.session.get('cart_pk')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
            try:
                order_pk = cart.order.pk
            except:
                order_pk = None

        obj, created = self.model.objects.get_or_create(
            pk = order_pk,
            defaults={
                'cart' : cart,
                'status' : False,
                'delivery_address' : "Пожалуйста заполните адрес",
                'contact_phone' : "Пожалуйста введите телефон",
            }
        )
        return obj
    
    def get_success_url(self):
        url = super().get_success_url()
        self.object.status = True
        self.object.save()
        del (self.request.session['cart_pk'])

        return url