from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_value = request.GET.get('sort')
    template = 'catalog.html'
    phone = 0
    if sort_value == 'min_price':
        phone = Phone.objects.order_by('price')
    elif sort_value == 'max_price':
        phone = Phone.objects.order_by('-price')
    elif sort_value == 'name':
        phone = Phone.objects.order_by('name')
    elif sort_value is None:
        phone = Phone.objects.order_by('id')
    context = {'phones': phone}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phones': phone}
    return render(request, template, context)
