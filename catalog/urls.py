from django.urls import path, include

from catalog.views import homepage

urlpatterns = [
    path('', homepage)
]
