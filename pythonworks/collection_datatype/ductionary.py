product={"id":1, "title":"diarymilk","price":40,"brand":"cadbury"}
product["price"]=100
print(product["price"])
product["brand"]="nestle"
product["used_by_time"]="10-03-2024"
# print(product)
if "offer" in product:
    product["offer"]=10

else:
    product["offer"]=20
    
print(product)