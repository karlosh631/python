import requests
import pandas as pd
import datetime
import json

url = "https://foodmandu.com/webapi/api/v2/Product/GetVendorProductsBySubCategoryV2?VendorId=1205&show="

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
   
        if isinstance(data, list):
            print("Here are the product names and prices:")
            products = []  
            for category in data:
                if "items" in category: 
                    for product in category["items"]:
                        name = product.get("name") 
                        price = product.get("price")  

                        if name and price is not None: 
                            print(f"{name}: {price}")
                            products.append({"Name": name, "Price": price})
            
            if products:
                df = pd.DataFrame(products)
                df.to_csv("products.csv", index=False)
                print("Product details saved to 'products.csv'.")
            else:
                print("No valid product data found to save.")
        else:
            print("Error: Unexpected data format.")
    else:
        print(f"Error: Received status code {response.status_code}.")
except requests.RequestException as e:
    print(f"Error in request: {e}")
