from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV

from pprint import pprint
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    context = {}
    file_gir = BUS_STATION_CSV
    with open(file_gir, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data = {'bus_stations': row['Name'], 'street': row['Street'], 'district': row['District']}
            context.update(data)
    pprint(context)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
    #     'bus_stations': ...,
    #     'page': ...,
    }
    return render(request, 'stations/index.html', context)
