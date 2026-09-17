from data.sales_data import sales

# Print the name of every product

for sale in sales:
    print(sale["product"])
print('------')

# Print only Electronics products

for sale in sales:
    if sale["category"] == "Electronics":
        print(sale["product"])
print('------')

# Print products with rating greater than 4.4

for sale in sales:
    if sale["rating"] >4.4:
        print(sale["product"])
print('------')

# Print products where quantity is more than 5

for sale in sales:
    if sale["quantity"] > 5:
        print(sale["product"])
print('------')

# Calculate the total number of products sold.

total_number_of_products = 0
for sale in sales:
    total_number_of_products = sale["quantity"] + total_number_of_products
print(f"The total number of products sold is {total_number_of_products}")
print('------')

# Calculate the total revenue of the store.

revenue = 0
total = 0
for sale in sales:
    revenue = sale["price"] * sale["quantity"]
    total = total + revenue
print(f"The total revenue of the sales is {total}")
print('-----')

# Find the product with the highest revenue.

highest_revenue = sales[0]["price"] * sales[0]["quantity"]
highest_revenue_product = sales[0]["product"]
for sale in sales:
    revenue = sale["price"] * sale["quantity"]
    if revenue > highest_revenue:
        highest_revenue = revenue
        highest_revenue_product = sale["product"]
print(f"The product with highest revenue is {highest_revenue} and it is {  highest_revenue_product }")
print('------')
# Calculate the total revenue from Electronics products only.

electronics_revenue = 0
for sale in sales:
    revenue = sale["price"] * sale["quantity"]
    if sale["category"] == "Electronics":
       electronics_revenue +=revenue
print(f"The total revenue for electronics products only is {electronics_revenue}")
print('------')

# Calculate the average product price.
total = 0
for sale in sales:
    total = total + sale["price"]
    average_price  = total / len(sales)
print(f"The average product price is {average_price}")
print('------')

# Calculate the average rating of all the products.

total_rating = 0
for sale in sales:
    total_rating = total_rating + sale["rating"]
    average_rating  = total_rating / len(sales)
print(f"The average rating of all the prducts is {average_rating}")
print('------')

# Calculate the total revenue for a specific city.

city_revenue = 0
for sale in sales:
    revenue = sale["price"] * sale["quantity"]
    if sale["city"] == "Stockholm":
        city_revenue += revenue
print(f"The total revenue from Stockholm city is {city_revenue}")
print('------')