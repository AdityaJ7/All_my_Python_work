import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.flipkart.com"
product = input("Enter a product of your choice: ").lower()
# product = "smartphones"
product_links = list()
product_offered_prices = list()
product_original_prices = list()
product_names = list()

for i in range(1, 4):  # In order to have atleast 50 records
    response = requests.get(f"{base_url}/search?q={product}&page={i}")
    soup = BeautifulSoup(response.text, "lxml")
    product_link_list = soup.find_all("a", class_="_1fQZEK")
    for product_link in product_link_list:
        product_links.append(base_url + product_link["href"])
    names = soup.find_all("div", class_="_4rR01T")
    for name in names:
        product_names.append(name.text.strip())
    offer_prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
    for offer_price in offer_prices:
        product_offered_prices.append(offer_price.text)
    original_prices = soup.find_all("div", class_="_3I9_wc _27UcVY")
    for original_price in original_prices:
        product_original_prices.append(original_price.text)

df = pd.DataFrame(
    {
        "Product Name": product_names,
        "Offered Price": product_offered_prices,
        "Original Price": product_original_prices,
        "Product Url": product_links,
    }
)

df.to_excel(f"Flipkart_{product}.xlsx", index=False)
