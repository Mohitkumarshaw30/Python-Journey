# Given a dictionary of products and their prices, find the product with the
# highest price.

products_price = {"A":12,"B":23,"C":14,"D":45}

high_price = 0

for product , price in products_price.items():
    current_price = price
    if (current_price > high_price):
        high_price = current_price
    
for product , price in products_price.items():
    if(price == high_price):
        print(product,":",price)




# or

products_price = {"A":12,"B":23,"C":14,"D":45}

highest_product = max(products_price, key=products_price.get)

print(highest_product, ":", products_price[highest_product])


