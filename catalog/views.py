import json
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product, Category


# Create your views here.
def homepage(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('data/contacts.json', 'a', encoding='utf-8') as file:
            json.dump({'name': name, 'phone': phone, 'message': message}, file)
    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product

# def products_list(request):
#     products = Product.objects.all()
#     categories = Category.objects.all()
#     content = {'cams': products, 'cctvs': categories}
#     return render(request, 'main/cam_list.html', content)


# def product_cam(request, pk):
#     cam = get_object_or_404(Product, pk=pk)
#     content = {'cam': cam}
#     return render(request, 'catalog/product_cam.html', content)

