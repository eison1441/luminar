product={"mobile":30,"soap":60,"alcohol":150}

new_product={items for items,values in product.items() if values>50}
print(new_product)




