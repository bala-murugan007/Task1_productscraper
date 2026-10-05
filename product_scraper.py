import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

print("Fetching product data...")

response = requests.get(url, timeout=20)
print("Status Code:", response.status_code)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
products = soup.select("article.product_pod")

data = []

for product in products:
    name = product.h3.a["title"]
    price = product.select_one(".price_color").get_text(strip=True)
    availability = product.select_one(".availability").get_text(strip=True)
    rating = product.select_one("p.star-rating")["class"][1]

    data.append({
        "Product Name": name,
        "Price": price,
        "Rating": rating,
        "Availability": availability
    })

with open("products_dataset.csv", "w", newline="", encoding="utf-8-sig") as file:
    columns = ["Product Name", "Price", "Rating", "Availability"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(data)

print("\nProduct Dataset:")
for item in data[:10]:
    print(item)

print("\nDataset created successfully!")
print("Total products:", len(data))
print("File name: products_dataset.csv")