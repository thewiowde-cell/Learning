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

# # Dicts
# # Task № 1
# users = [
#     {"name": "Иван", "age": 25},
#     {"name": "Мария", "age": 17},
#     {"name": "Алексей", "age": 30},
#     {"name": "Оля", "age": 16}
# ]

# adult_users = [user for user in users if user['age'] > 18]

# names = [user['name'] for user in adult_users]
# print("Adult user names:", names)

# if adult_users:
#     avg_age = sum(user['age'] for user in adult_users) / len(adult_users)
#     print("Average age:", round(avg_age, 2))
# else:
#     print("No adult users found")

# # # Task № 2
# products = [
#     {"name": "iPhone", "price": 500},
#     {"name": "Samsung", "price": 450},
#     {"name": "Xiaomi", "price": 300},
#     {"name": "iPhone", "price": 500}
# ]

# unique_products = {
#     (p['name'], p['price']): p
#     for p in products
# }.values()

# unique_products = list(unique_products)

# if unique_products:
#     most_expensive = max(unique_products, key=lambda x: x['price'])
#     avg_price = sum(p['price'] for p in unique_products) / len(unique_products)

#     print("Most expensive:", most_expensive)
#     print("Average price:", round(avg_price, 2))
# else:
#     print("No products found")

# # Task № 3
# data = [
#     "iPhone - 500$",
#     "Samsung - 450$",
#     "Xiaomi - 300$"
# ]

# product_list = []

# for item in data:
#     try:
#         name, price = item.replace('$', '').split(' - ')
#         price = int(price)

#         product_list.append({
#             'name': name,
#             'price': round(price * 1.1)
#         })

#     except Exception as e:
#         print(f"Error processing item: {item}")

# print("Product list: ", product_list)

# # Task № 4
# from collections import defaultdict

# data = [
#     {"category": "phone", "price": 500},
#     {"category": "laptop", "price": 1000},
#     {"category": "phone", "price": 300},
#     {"category": "laptop", "price": 1500}
# ]

# category_prices = defaultdict(list)

# for item in data:
#     category_prices[item['category']].append(item['price'])

# print("Category prices: ", category_prices)

# # Task № 5
# data = [
#     {"name": "Company A", "email": "a@mail.com"},
#     {"name": "Company B", "email": None},
#     {"name": "Company C", "email": "c@mail.com"},
#     {"name": "Company A", "email": "a@mail.com"}
# ]

# unique_companies = {}
# unique_emails = set()

# for item in data:
#     name = item['name']
#     email = item['email']

#     if not email:
#         continue

#     unique_emails.add(email)

#     if name not in unique_companies:
#         unique_companies[name] = [email]

# print("Only_emails: ", list(unique_emails))

# # Mini Challenge
# from collections import defaultdict

# orders = [
#     {"user": "Иван", "amount": 100},
#     {"user": "Мария", "amount": 200},
#     {"user": "Иван", "amount": 50}
# ]

# individual_expenses = defaultdict(int)

# for human in orders:
#     individual_expenses[human['user']] += human['amount']

#     if not human['user'] or not isinstance(human['amount'], (int, float)):
#         continue

# print("Individual expenses: ", dict(individual_expenses))

# # Working with files
# from pathlib import Path

# files_dir = Path('files')
# files_dir.mkdir(exist_ok=True)

# first_file = files_dir / 'first.txt'
# second_file = files_dir / 'second.txt'

# with open(first_file, 'w') as my_file:
#     my_file.write("First string\n")
#     my_file.write("Second string\n")
#     my_file.write("Third string\n")


# with open(second_file, 'w') as my_file:
#     lines = [
#         "First line in the second file",
#         "Second line in the second file",
#         "Third line in the second file",
#     ]

#     for line in lines:
#         my_file.write(line + '\n')

# with open(first_file) as my_file:
#     print(my_file.read())

# with open(second_file) as my_file:
#     for line in my_file:
#         print(line.strip())

# first_file.unlink()
# second_file.unlink()

# files_dir.rmdir()

# import csv

# with open('test.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file, delimiter=';')
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])
#     writer.writerow([5432, 'Mikhail', 1234])
#     writer.writerow([8378, 'Lenin', 212])
#     writer.writerow([1347, 'Stalin', 21])

# with open('test.csv') as csv_file:
#     reader = csv.reader(csv_file, delimiter=';')
#     for line in reader:
#         if line:
#             converted_line = []
#             for item in line:
#                 try:
#                     converted_line.append(int(item))
#                 except ValueError:
#                     converted_line.append(item)
#             print(converted_line)

# def image_info(my_dict):
#     if not isinstance(my_dict, dict):
#         raise ValueError("This argument is not a dictionary")

#     keys_dict = my_dict.keys()

#     if 'image_id' not in keys_dict and 'image_title' not in keys_dict:
#         raise TypeError(
#             "The keys 'image_id' and 'image_title' is not present in this argument")

#     if 'image_id' not in keys_dict:
#         raise TypeError("The key 'image_id' is not present in this argument")

#     if 'image_title' not in keys_dict:
#         raise TypeError(
#             "The key 'image_title' is not present in this argument")

#     return print(f"Image {my_dict['image_title']} has id {my_dict['image_id']}")


# first_dict = {'image_id': 5136, 'image_title': 'my cat', 'name': 'Mikhail'}
# second_dict = {'image_title': 'my cat'}
# third_dict = {'image_id': 5136}
# fourth_dict = {}
# notdict = 1

# try:
#     # image_info(first_dict)
#     # image_info(second_dict)
#     # image_info(third_dict)
#     # image_info(fourth_dict)
#     image_info(notdict)
# except Exception as e:
#     print(e)
