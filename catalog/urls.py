from django.urls import path
from catalog.views import ContactsView, ProductListView, ProductDetailView, BlogListView, BlogCreateView, \
    BlogUpdateView, BlogDetailView, BlogDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_blog'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
