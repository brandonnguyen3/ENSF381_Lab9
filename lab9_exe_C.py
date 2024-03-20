import requests
import json

def fetch_product_data(url):
    try: 
        response = requests.get(url)
        response.raise_for_status ()
        return response.json () ['products']
    except requests.exceptions.RequestException as e :
        print(f"Error fetching data: {e}")
        return None
    
def list_all_products(products):
    #complete this function

def search_product(products, name):
    for product in products:
        pass
        #complete the for loop.
        #it must pretty print the product details with 4 indents

    print("Product not found")


def main():
    products_url = ' https://dummyjson.com/products'
    products = fetch_product_data (products_url)

    if products:
        while True:
            choice = input(" Choose an option:\n1.List all products\n2.Search for a product \n3.Exit\n>")
            if choice == '1':
                pass
                #complete the code
                #call suitable function(s)
            
            elif choice == '2':
                product_name = input (" Enter the product name : ")
                #Complete the code
                #call suitable functions(s)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Failed to fetch product data.")

if __name__ == "__main__":
    main()

