products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Smartphone", "Tablet"]
price_dict = {"Laptop": 80000, "Smartphone": 20000, "Tablet": 30000, "Smartwatch": 15000, "Headphones": 5000, "Charger": 2000, "Camera": 40000, "Mouse": 0, "Keyboard": 0, "Monitor": 0}
category_list = ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics", "Electronics"]
catalog = []

for i in range(len(products)):
    name = products[i]
    price = price_dict.get(name, 0)
    category = category_list[i]
    catalog.append({"Name": name, "Price": price, "Category": category})

for item in catalog:
    print(item)

category_to_products = {}
for item in catalog:
    category = item["Category"]
    name = item["Name"]
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(name)

for category, items in category_to_products.items():
    print(f"Category: {category}, Products: {items}")
    
max_category = max(category_to_products, key=lambda c: len(category_to_products[c]))

print(f"Products in the largest category ({max_category}):")
for product in category_to_products[max_category]:
    print("-", product)
