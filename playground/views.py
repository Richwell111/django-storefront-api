from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product


def say_hello(request):
    # try:
    #     # raise ObjectDoesNotExist()
    #     # product = Product.objects.get(pk=1)
    #     # print(product)
    #     pass
    # except ObjectDoesNotExist:
    #     pass
    queryset = Product.objects.filter(unit_price__gt=20)

    return render(request, 'hello.html', {'name': 'Richman', 'products': queryset})
