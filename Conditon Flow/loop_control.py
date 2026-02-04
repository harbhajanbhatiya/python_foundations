daily=[200,150,0,400,50,-1,300]
sales=0
for sale in daily:
    if sale==-1:
        print("Corrupt data found, stopping processing")
        break
    elif sale==0:
        print("No sales recorded for the day, skipping to next day")
        continue
    else:
        sales+=sale
        print(f"Total sales recorded: {sales}")