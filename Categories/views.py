from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .models import *
from rest_framework.permissions import AllowAny

class CategoryViewSet(ModelViewSet):
    serializer_class = categoryserializer
    queryset = category.objects.all()
    permission_classes = [AllowAny]
    # pagination_class = CursorPagination


class ProductViewSet(ModelViewSet):
    serializer_class = productsserializer
    queryset = products.objects.all()
    permission_classes = [AllowAny]

@csrf_exempt
def Product(request):
    category = request.GET.get('name', None)
    print("--->", category)
    queryset = list(products.objects.filter(category_name__name__iexact=category).values())

    if not queryset:
        queryset = 'No Data Found'
    return JsonResponse({'Products': queryset})

    permission_classes = [AllowAny]


def Home(request):
    ctx = {}
    queryset = category.objects.all()
    ctx['data'] = queryset
    # print(ctx)
    return render(request, 'categories.html', ctx)

def Products(request, id):
    ctx = {}
    product = products.objects.filter(category=id)
    ctx['data'] = product
    print(ctx)
    # ctx['category'] = "Jeans"
    ctx['category'] = category.objects.get(id=id)
    # print(ctx)
    return render(request, 'products.html', ctx)
    return render(request, 'navbar.html', ctx)

def Product_Details(request, id):
    ctx = {}
    product = products.objects.filter(id=id)
    ctx['data'] = product
    # print(ctx)
    # ctx['category'] = category.objects.get(id=id)
    # ctx['category'] = "Jeans"
    # ctx['category'] = category.objects.get(id=id)
    # return JsonResponse({'data': 'ctx'})
    return render(request, 'product_details.html', ctx)
