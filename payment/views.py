from django.shortcuts import render, get_object_or_404
from cart import cart
from .models import Order
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def payment_done(request):
    return render(request,'done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request,'canceled.html')



def payment_process(request):
    cart_id = request.session.get('cart_id')
    Items = cart.get_cart_items(request)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount' : '%.2f' % cart.cart_subtotal(request).quantize(Decimal('.01')),
        'item_name' : str(Items),
        'invoice': str(cart_id),
        'currency_code' : 'USD',
        #"notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        #"return": request.build_absolute_uri(reverse('payment:payment_done')),
        #"cancel_return": request.build_absolute_uri(reverse('payment:payment_canceled')),
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
       'return_url': 'http://{}{}'.format(host, reverse('payment:payment_done')),
       'cancel_return': 'http://{}{}'.format(host, reverse('payment:payment_canceled')),

    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process.html', {'form': form })
