# # Lists
# # Task № 1
# numbers = [5, 12, 7, 20, 3, 15]
# filtered = [i for i in numbers if i > 10]

# print("Numbers > 10: ", filtered)

# if filtered:
#     print("Sum: ", sum(filtered))
#     print("Max: ", max(filtered))
# else:
#     print("No numbers greater than 10 found.")

# # Task № 2
# names = ["Иван", "Мария", "Алексей", "Оля", "Дмитрий"]

# filtered_names = [name for name in names if len(name) > 4]

# if filtered_names:
#     print("Names with more than 4 characters: ", filtered_names)
#     print("Count: ", len(filtered_names))
# else:
#     print("No names with more than 4 characters found.")

# # Task № 3
# prices = ["100 руб", "250 руб", "80 руб", "320 руб", "150 руб"]

# numbers = [int(price.replace(" руб", "")) for price in prices]

# increased_prices = [price * 1.2 for price in numbers]

# if increased_prices:
#     print("Prices increased by 20%: ", increased_prices)
#     print("Average value: ", sum(increased_prices)/len(increased_prices))
# else:
#     print("No prices found.")

# # Task № 4
# data = ["apple", "banana", "apple", "orange", "banana", "apple"]

# apple_count = data.count("apple")
# print("Number of times 'apple' appears: ", apple_count)

# unique_fruits = []

# for fruit in data:
#     if fruit not in unique_fruits:
#         unique_fruits.append(fruit)

# print("Unique fruits: ", unique_fruits)

# # Mini challenge
# numbers = [1, 2, 3, 4, 5, 6]

# new_numbers = [i * 2 for i in numbers if i % 2 == 0]

# print("New numbers: ", new_numbers)

# # Task № 5
# data = [
#     "iPhone 13 - 500$",
#     "Samsung S21 - 450$",
#     "iPhone 13 - 500$",
#     "Xiaomi Mi 11 - 300$"
# ]

# products = []

# for item in data:
#     name, price = item.split(" - ")
#     price = int(price.replace("$", ""))
#     products.append((name, price))

# unique_products = []

# for product in products:
#     if product not in unique_products:
#         unique_products.append(product)

# average_price = sum([p[1] for p in unique_products]) / len(unique_products)
# max_price = max(unique_products, key=lambda x: x[1])


# print("Unique products: ", unique_products)
# print("Average price: ", average_price)
# print("Max price: ", max_price)

# Dicts
# Task № 1
users = [
    {"name": "Иван", "age": 25},
    {"name": "Мария", "age": 17},
    {"name": "Алексей", "age": 30},
    {"name": "Оля", "age": 16}
]

adult_users = [user for user in users if user['age'] > 18]
print("Adult users: ", adult_users)
