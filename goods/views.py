from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from goods.models import Products, Categories
from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    current_category_name = "Все товары"

    if category_slug == 'all':
        goods = Products.objects.all()
        current_category_name = "Все товары"
    elif query:
        goods = q_search(query)
        current_category_name = f"Поиск: {query}"
    else:
        category = get_object_or_404(Categories, slug=category_slug)
        current_category_name = category.name
        goods = Products.objects.filter(category=category)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 6) 
    current_page = paginator.page(int(page))       

    context = {
        "title": "DRY Tech - каталог", 
        "goods": current_page, 
        "slug_url": category_slug,
        "current_category_name": current_category_name,
        "is_on_sale_active": bool(on_sale), 
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)