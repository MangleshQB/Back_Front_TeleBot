from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
