from django.urls import path

from catalog.views import homepage, contacts, products_list

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', homepage, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products_list, name='products')
]
