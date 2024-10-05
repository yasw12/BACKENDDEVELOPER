import csv


def find_minimum_price(csv_file, food_items):
    food_items = food_items.split()

    restaurants = {}

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            restaurant_id = int(row['restaurant_id'])
            food_item_name = row['food_item_name']
            food_item_price = float(row['food_item_price'])


            if restaurant_id not in restaurants:
                restaurants[restaurant_id] = {}

            restaurants[restaurant_id][food_item_name] = food_item_price

    min_price = float('inf')
    min_restaurant_id = None

    for restaurant_id, menu in restaurants.items():
        if all(item in menu for item in food_items):
            total_price = sum(menu[item] for item in food_items)
            if total_price < min_price:
                min_price = total_price
                min_restaurant_id = restaurant_id

    if min_restaurant_id is not None:
        return f"{min_restaurant_id}, {min_price:.2f}"
    else:
        return "No matching restaurant found"



input_1 = find_minimum_price('data.csv', 'burger tofu_log')
print(input_1)

input_2 = find_minimum_price('data.csv', 'chef_salad wine_spritzer')
print(input_2)

input_3 = find_minimum_price('data.csv', 'extreme_fajita jalapeno_poppers extra_salsa')
print(input_3) 
