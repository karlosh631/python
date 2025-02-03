import requests


url="https://foodmandu.com/webapi/api/v2/Product/GetVendorProductsBySubCategoryV2?VendorId=1205&show="
try:
    response = requests.get(url)
 
    if response.status_code == 200:
       
        print(response.json())  
    else:
        print("error")
except requests.RequestException as e:
    print("error occured on requests e:")


