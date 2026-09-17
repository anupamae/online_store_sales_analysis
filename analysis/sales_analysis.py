from data.sales_data import sales

def total_revenue(sales):
    total = 0
    for sale in sales:
        revenue = sale["price"] * sale["quantity"]
        total = total + revenue
    return total

def highest_revenue_product(sales):
    highest_revenue =sales[0]["price"] * sales[0]["quantity"]
    highest_revenue_product =sales[0]["product"]

    for sale in sales:
        revenue = sale["price"] * sale["quantity"]
        if revenue>highest_revenue:
            highest_revenue = revenue
            highest_revenue_product = sale["product"]
    return highest_revenue_product

def electronics_revenue(sales):
    electronics_revenue = 0
    for sale in sales:
        revenue = sale["price"] * sale["quantity"]
        if sale["category"] == "Electronics":
            electronics_revenue += revenue
    return f"the total electronics revenue is {electronics_revenue}"

def average_product_price(sales):
    average = 0
    total = 0
    for sale in sales :
        total = total + sale["price"]
    average = total/len(sales)
    return f"The average product price is {average}"

def average_rating(sales):
    total_rating = 0
    for sale in sales:
        total_rating = total_rating + sale["rating"]
    average_rating = total_rating / len(sales)
    return average_rating

def city_revenue(sales, city):
    city_revenue = 0
    for sale in sales:
        revenue = sale["price"] * sale["quantity"]
        if sale["city"] == city:
            city_revenue += revenue
    return city_revenue

def highest_rated_product(sales):
    high_rate = sales[0]["rating"]
    high_rate_product = sales[0]["product"]
    for sale in sales:
        if sale["rating"] > high_rate:
            high_rate = sale["rating"]
            high_rate_product = sale["product"]
    return f" {high_rate_product}, {high_rate}"

def products_by_category(sales, category):
    category_list= []
    for sale in sales:
        if sale["category"] == category:
            category_list.append(sale["product"])
    return category_list

def most_sold_product(sales):
    most_sold = sales[0]["quantity"]
    most_sold_product = sales[0]["product"]
    for sale in sales:
        if sale["quantity"] > most_sold:
            most_sold = sale["quantity"]
            most_sold_product = sale["product"]
    return f"{most_sold_product} - {most_sold}"

def revenue_by_category(sales):
    electronics_total = 0
    furniture_total = 0
    for sale in sales:
        revenue = sale["price"] * sale["quantity"]
        if sale["category"] == "Electronics":
            electronics_total += revenue
        elif sale["category"] == "Furniture":
            furniture_total += revenue
    return f"Electronics - {electronics_total}\nFurniture - {furniture_total}"

def products_above_average_price(sales):
    total = 0
    products = []
    for sale in sales:
        total = total + sale["price"]
    average_price = total / len(sales)

    for sale in sales:
        if sale["price"] > average_price:
            products.append(sale["product"])
    return products

def sales_report(sales):
    print("\n========== SALES REPORT ==========")
    print(f"Total Revenue - {total_revenue(sales)}")
    print(f"Highest Revenue Product - {highest_revenue_product(sales)}")
    print(f"Average rating - {average_rating(sales)}")
    print(f"Highest rated product - {highest_rated_product(sales)}")
    print(f"Revenue by category:\n{revenue_by_category(sales)}")