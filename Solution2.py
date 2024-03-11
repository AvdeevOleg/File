# -*- coding: cp1251 -*-
def create_cook_book_from_file(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            file.readline()  # Пропускаем пустую строку между блюдами
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
    return shop_list

# Создаем кулинарную книгу из файла
cook_book = create_cook_book_from_file('recipes.txt')

# Получаем список покупок для указанных блюд и количества персон
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)

from collections import OrderedDict

# Выводим список покупок
print("{")
for ingredient, info in OrderedDict(sorted(shop_list.items())).items():
    print(f"  '{ingredient}': {{'measure': '{info['measure']}', 'quantity': {info['quantity']}}},")
print("}")