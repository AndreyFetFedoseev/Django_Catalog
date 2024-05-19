import json
from django.shortcuts import render
from catalog.models import Product, Category


# Create your views here.
def homepage(request):
    return render(request, 'main/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('data/contacts.json', 'a', encoding='utf-8') as file:
            json.dump({'name': name, 'phone': phone, 'message': message}, file)
    return render(request, 'main/contacts.html')


# def product(request):
#     return render(request, 'main/product.html')


def products_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    content = {'cams': products, 'cctvs': categories}
    return render(request, 'main/cam_list.html', content)
