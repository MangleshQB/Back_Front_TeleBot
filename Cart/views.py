from django.shortcuts import render

# Create your views here.
# class Cart(View):
#     def get(self , request):
#         ids = list(request.session.get('cart').keys())
#         products = pro.get_products_by_id(ids)
#         print(products)
#         return render(request , 'cart.html' , {'products' : products} )