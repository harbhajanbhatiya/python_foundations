products=["Laptop", "Mouse", "Keyboard", "Monitor","Smartphone", "Tablet","Smartphone","Monitor","Monitor","Smartphone", "Tablet"]
categories_set=set(products)
categories_set.add("Smartwatch")
categories_set.add("Keyboard")
print(f"Categories set: {categories_set}")
is_present="Tablet" in categories_set
print(f"Is 'Tablet' present in categories set? {is_present}")
unique_count=len(categories_set)
total_products=len(products)
print(f"Total products list: {total_products}")
print(f"Number of unique categories: {unique_count}")
