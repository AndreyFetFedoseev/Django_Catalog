import json

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm
# from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Category, Blog, Version


# Create your views here.
# class HomePageView(TemplateView):
#     template_name = 'catalog/index.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            with open('data/contacts.json', 'a', encoding='utf-8') as file:
                json.dump({'name': name, 'phone': phone, 'message': message}, file)
        return super().get_context_data(**kwargs)


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        # context['versions'] = Version.objects.all()
        # context['versions'] = get_object_or_404(Version, pk=self.kwargs.get('pk'))
        return context


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview')
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        if form.is_valid():
            blog = form.save()
            blog.slug = slugify(blog.title)
            blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview')

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:home')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object

# def homepage(request):
#     return render(request, 'catalog/index.html')

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         with open('data/contacts.json', 'a', encoding='utf-8') as file:
#             json.dump({'name': name, 'phone': phone, 'message': message}, file)
#     return render(request, 'catalog/contacts.html')

# def products_list(request):
#     products = Product.objects.all()
#     categories = Category.objects.all()
#     content = {'cams': products, 'cctvs': categories}
#     return render(request, 'main/cam_list.html', content)


# def product_cam(request, pk):
#     cam = get_object_or_404(Product, pk=pk)
#     content = {'cam': cam}
#     return render(request, 'catalog/product_cam.html', content)
