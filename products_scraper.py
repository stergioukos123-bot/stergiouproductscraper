import requests
from bs4 import BeautifulSoup

# URL του site
url = "https://books.toscrape.com/"

# Κατεβάζουμε τη σελίδα
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Βρίσκουμε όλα τα προϊόντα
products = soup.find_all("article", class_="product_pod")

# Παίρνουμε όνομα και τιμή
for product in products:
    name = product.h3.a['title']
    price = product.find("p", class_="price_color").text
    print(f"{name} --> {price}")
