from django.urls import path
from . import views


urlpatterns = [
    path('all_products/', views.product_all, name="all_products"),
    path('product/<int:id>/', views.product_detail, name='product_detail')
]
