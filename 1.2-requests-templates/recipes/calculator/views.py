from django.http import HttpResponse
from django.shortcuts import render

from pprint import pprint

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'casserole': {
        'картофельное пюре, г': 200,
        'фарш говяжий, г': 100,
        'яйцо, шт': 0.5,
        'масло сливочное, г': 10,
        'овощи консервированные/замороженные, г': 40,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def show_recipes(request, recipe):
    servings = int(request.GET.get('s', 1))
    context = {}
    if recipe in DATA.keys():
        context = {
            'recipe': DATA[recipe]
        }
    for i in context.values():
        for j in i.keys():
            i[j] = i.get(j)*servings
    return render(request, 'calculator/index.html', context)
