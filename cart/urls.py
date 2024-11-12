from django.urls import path
from .views import add_to_cart, cart_view, remove_from_cart,checkout,payment_success

app_name = 'cart'
urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('checkout/success/', payment_success, name='payment_success'),
]