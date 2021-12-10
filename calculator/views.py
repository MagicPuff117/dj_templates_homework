from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
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

def all_recipies_view(request):
    all_recipies = list(DATA.keys())


    context = {
        'all_recipies': all_recipies
    }

    return render(request, 'all_recipies.html', context)



def recipe_view(request, recipe_name):
    if recipe_name in DATA:
        data = DATA[recipe_name]
        servings = request.GET.get('servings', None)
        if servings:
            result = dict()
            for i, v in data.items():
                new_v = v * int(servings)
                result[i] = new_v

            context = {
                'recipe': result
            }
        else:
            context = {
                'recipe': data
            }

    else:
        context = Noned
    return render(request, 'index.html', context=context)

