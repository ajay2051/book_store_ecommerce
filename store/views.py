from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Create your views here.

def categories(request):
    return {
        "categories": Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/home.html', context=context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, in_stock=True)
    context = {
        'product': product
    }
    return render(request, 'store/products/detail.html', context=context)


def category_list(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'store/products/category.html', context=context)
