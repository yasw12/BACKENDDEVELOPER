import csv
from collections import defaultdict


def find_minimum_price(filename, food_items):

    restaurant_data = defaultdict(dict)


    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')  # Using tab ('\t') delimiter based on provided format
        for row in reader:
            restaurant_id = int(row['restaurant_id'])
            food_item_name = row['food_item_name']
            food_item_price = float(row['price'])
            restaurant_data[restaurant_id][food_item_name] = food_item_price


    min_price = float('inf')
    min_restaurant = None

    for restaurant_id, items in restaurant_data.items():

        if all(food in items for food in food_items):
            total_price = sum(items[food] for food in food_items)
            if total_price < min_price:
                min_price = total_price
                min_restaurant = restaurant_id

    # Return the result
    if min_restaurant is not None:
        return min_restaurant, round(min_price, 2)
    else:
        return "No matching restaurant found"

food_items = ["burger", "tofu_log"]
result = find_minimum_price('data.csv', food_items)
print(result)
food_items = ["chef_salad", "wine_spritzer"]
result = find_minimum_price('data.csv', food_items)
print(result)
