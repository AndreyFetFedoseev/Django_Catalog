from django.urls import path

from catalog.views import homepage, contacts

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', homepage),
    path('contacts/', contacts)
]
