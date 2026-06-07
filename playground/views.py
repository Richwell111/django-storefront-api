from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from django.db.models import Q,Func,Value, F

from store.models import Collection, Customer, Order, Product


def say_hello(request):
    # try:
    #     # raise ObjectDoesNotExist()
    #     # product = Product.objects.get(pk=1)
    #     # print(product)
    #     pass
    # except ObjectDoesNotExist:
    #     pass
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    order=Order()
    order.customer_id=1
    order.save()
    return render(request, 'hello.html', {'name': 'Richman', 'result': list(queryset)})
