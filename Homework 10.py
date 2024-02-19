
# დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის გამოყენებით "https://fakestoreapi.com/products" მისამართზე, 
# შეამოწმებს სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:


# ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები

# import requests

# def get_product_prices():
#     url = "https://fakestoreapi.com/products"


#     response = requests.get(url)

#     if response.status_code == 200:
    
#         products = response.json()

#         prices = [product['price'] for product in products]

#         max_price = max(prices)
#         min_price = min(prices)
#         avg_price = sum(prices) / len(prices)

#         print(f"Maximum price: ${max_price}")
#         print(f"Minimum price: ${min_price}")
#         print(f"Average price: ${avg_price:.2f}")
#     else:
#         print("Failed to fetch data")

# get_product_prices()




# ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ

# import requests

# def get_unique_sorted_categories():
#     url = "https://fakestoreapi.com/products"

#     response = requests.get(url)

#     if response.status_code == 200:
#         products = response.json()

#         categories = set()

#         for product in products:
#             categories.add(product['category'])

#         sorted_categories = sorted(categories)

#         print("Sorted  categories:")
#         for category in sorted_categories:
#             print(category)
#     else:
#         print("Failed to data")

# get_unique_sorted_categories()




# გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით

# import requests

# def get_sorted_product_description_and_id():
#     url = "https://fakestoreapi.com/products"

#     response = requests.get(url)

#     if response.status_code == 200:

#         products = response.json()

#         products_info = [{'title': product['title'], 'id': product['id']} for product in products]

#         sorted_products_info = sorted(products_info, key=lambda x: x['title'])

#         print("Sorted product descriptions and IDs:")
#         for product in sorted_products_info:
#             print(f"Title: {product['title']}, ID: {product['id']}")
#     else:
#         print("Failed to fetch data")

# get_sorted_product_description_and_id()



# დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით


import requests

def get_sorted_ratings():
    url = "https://fakestoreapi.com/products"


    response = requests.get(url)

    if response.status_code == 200:
        
        products = response.json()

       
        ratings = [product['rating'] for product in products]

       
        sorted_ratings = sorted(ratings)

        print("Sorted ratings in ascending order:")
        for rating in sorted_ratings:
            print(rating)
    else:
        print("Failed to fetch data")


get_sorted_ratings()




