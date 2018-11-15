from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from .models import Category, Product
from .forms import *

# from django.template import RequestContext
# from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.urls import reverse
from cart import cart
from .forms import ProductAddToCartForm


# Create your views here.
def index(request):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render(request, 'catalog/index.html', {'page_title': page_title})


def show_category(request, category_slug=None):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render(request, 'catalog/category.html', {'c': c, 'products': products, 'page_title': page_title,
                                                     'meta_keywords': meta_keywords, 'meta_description': meta_description })


def show_product(request, product_slug=None):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    # need to evaluate the HTTP method
    if request.method == 'POST':
        # add to cart..create  the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        # check if posted data is valid
        if form.is_valid():
            # add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
        return HttpResponseRedirect(reverse('cart:show_cart'))
    else:
        # it’s a GET, create the unbound form. Note request as a kwarg
        form = ProductAddToCartForm(request=request, label_suffix=':')
        # assign the hidden input the product slug
        form.fields['product_slug'].widget.attrs['value'] = product_slug
        # set the test cookie on our first GET request
        request.session.set_test_cookie()
    return render(request, 'catalog/product.html', {'p': p, 'form': form, 'categories': categories,
                                                    'page_title': page_title, 'meta_description': meta_description,
                                                    'meta_keywords': meta_keywords})
