from django.urls import path
from catalog.views import homepage, contacts, products_list, product_cam
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', homepage, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products_list, name='products'),
    path('products/<int:pk>/', product_cam, name='cam_product'),
]
