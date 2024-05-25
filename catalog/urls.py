from django.urls import path
from catalog.views import homepage, contacts, ProductListView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', homepage, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
