from django.urls import path
from . import views
from .views import products_by_category_view

urlpatterns = [
    path('', views.store, name="store"),
    path('category/<category>', products_by_category_view,
         name='products_by_category'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
