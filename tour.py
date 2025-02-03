
import requests
from bs4 import BeautifulSoup


url = "https://www.trekandtrails.com/"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Web content extracted successfully")
        
        soup = BeautifulSoup(response.text, 'html.parser')  
        
        text= soup.get_text(strip=True)
        print("\n All the text")
        
        
        
        links = soup.find_all('a')
        print("\n All Links ")
        for link in links:
            href = link.get('href')
            if href:  
                print(href)
        
    
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        print("\n All Headings")
        for heading in headings:
            print(heading.text.strip())
        
        
        paragraphs = soup.find_all('p')
        print("\n  All Paragraphs ")
        for paragraph in paragraphs:
            print(paragraph.text.strip())
        
       
        images = soup.find_all('img')
        print("\n  All Images ")
        for img in images:
            src = img.get('src')
            if src:
                print(src)

       
    else:
        print(f"Error: Received status code {response.status_code}.")
except requests.RequestException as e:
    print(f"Error in request: {e}")
