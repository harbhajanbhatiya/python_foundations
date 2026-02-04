products=["Laptop", "Mouse", "Keyboard", "Monitor","Smartphone", "Tablet"]
sample_products=("Laptop",56000,"Electronics")
print(f"Second product in the list: {products[1]}")
print(f"Last product in the list: {products[-1]}")
products.append("Smartwatch")
products.append("Headphones")
print(f"Products after adding new items: {products}")
temp_list=list(sample_products)
temp_list[1]=90000  
sample_products=tuple(temp_list)
print(f"Modified sample product tuple: {sample_products}")  