def read_recipes_from_file(file_name, num_dishes=3):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for _ in range(num_dishes):
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split('|')
                ingredient_name = ingredient_info[0].strip()
                quantity = int(ingredient_info[1].strip())
                measure = ingredient_info[2].strip()
                ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book


cook_book = read_recipes_from_file('recipes.txt', num_dishes=3)
for dish, ingredients in cook_book.items():
    print(dish)
    for ingredient in ingredients:
        print(ingredient)
    print()
