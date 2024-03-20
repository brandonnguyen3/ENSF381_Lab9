import requests
import json

def fetch_product_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['products']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def list_all_products(products):
    print("All Products:")
    for product in products:
        print(f" - {product['title']}") # Pretty print with 4 indents.

def search_product(products, name):
    for product in products:
        if product['title'].lower() == name.lower():
            print("Product Found:")
            print_product_details(product)
            return
    print("Product not found")

def print_product_details(product):
    print("ID:", product["id"])
    print("Title:", product["title"])
    print("Description:", product["description"])
    print("Price:", product["price"])
    print("Discount Percentage:", product["discountPercentage"])
    print("Rating:", product["rating"])
    print("Stock:", product["stock"])
    print("Brand:", product["brand"])
    print("Category:", product["category"])
    print("Thumbnail:", product["thumbnail"])
    print("Images:")
    for image in product["images"]:
        print("  -", image)

def main():
    products_url = 'https://dummyjson.com/products'
    products = fetch_product_data(products_url)

    if products:
        while True:
            print("\nChoose an option:")
            print("1. List all products")
            print("2. Search for a product")
            print("3. Exit")
            choice = input(">")
            
            if choice == '1':
                list_all_products(products) # Call function to list all products
            elif choice == '2':
                product_name = input("Enter the product name: ")
                search_product(products, product_name) # Call function to search for a product
            elif choice == '3':
                break # Exit the loop if user chooses to exit
            else:
                print("Invalid choice. Please try again.") # Print message for invalid input

    else:
        print("Failed to fetch product data.") # Print message if product data fetching fails

if __name__ == "__main__":
    main()
