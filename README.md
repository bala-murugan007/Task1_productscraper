# Product Scraper - CodeAlpha Task 1

## Project Overview
This project is a web scraping application developed using Python. It extracts product information from a demo online bookstore website and stores the collected data in a CSV file.

## Objective
The main objective of this project is to collect product details automatically from a website and organize the information into a structured dataset for further analysis.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- CSV Module

## Data Source
Website: https://books.toscrape.com/

Books to Scrape is a demo website used for practicing web scraping.

## Features
- Extracts product names
- Collects product prices
- Retrieves product ratings
- Checks product availability
- Saves scraped data into a CSV file
- Displays the collected product information in the terminal

## How It Works
1. The program sends a request to the demo bookstore website.
2. BeautifulSoup parses the webpage HTML.
3. Product names, prices, ratings, and availability are extracted.
4. The extracted information is organized into a structured dataset.
5. The dataset is saved as `products_dataset.csv`.

## Project Files
- `product_scraper.py` - Python source code for web scraping.
- `products_dataset.csv` - Dataset containing scraped product details.
- `README.md` - Project documentation.

## Installation

Install the required libraries using:

```bash
py -m pip install requests beautifulsoup4
```

## How to Run

Run the following command in the terminal:

```bash
py product_scraper.py
```

## Output
The program successfully scraped 20 products from the demo bookstore website and saved the collected information in `products_dataset.csv`.

The dataset contains:
- Product Name
- Price
- Rating
- Availability

## Conclusion
This project demonstrates how Python can be used to automate web scraping and collect structured information from a website. The extracted data is stored in CSV format for easy access and further analysis.

## Author
M. Bala Murugan

## Internship
CodeAlpha Internship - Task 1: Web Scraping