from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from basket.basket import Basket
from store.models import Product


# Create your views here.

def basket_summary(request):
    basket = Basket(request)
    context = {
        'basket': basket
    }
    return render(request, 'store/basket/summary.html', context=context)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))  # product_id same name as in ajax function
        product_qty = int(request.POST.get('product_qty'))  # product_qty same name as in ajax function
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({'qty': basket_qty})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        basket.update(product=product_id, qty=product_qty)

        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        response = JsonResponse({"qty": basket_qty, "subtotal": basket_total})  # qty and subtotal same as in ajax
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        basket.delete(product=product_id, )

        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        response = JsonResponse({'qty': basket_qty, 'subtotal': basket_total})  # qty and subtotal same as in ajax
        return response
