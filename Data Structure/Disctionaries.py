price_dict={"Laptop":80000,"Mobile":20000,"Tablet":30000,"Smartwatch":15000,"Headphones":5000,"Charger":2000,"Camera":40000}
price_dict["Smartphone"]=25000  #Adding New product
price_dict["Laptop"]=75000

removed_item=price_dict.pop("Charger")  #Removing an item
print("Removed Item Price:",removed_item)
avg_price=sum(price_dict.values())/len(price_dict)
print("Average Price of Products:",avg_price)

max_price_item=max(price_dict,key=price_dict.get)
min_price_item=min(price_dict,key=price_dict.get)
print("Most Expensive Product:",max_price_item,price_dict[max_price_item])
print("Least Expensive Product:",min_price_item,price_dict[min_price_item])