# tokopedia-scrapers

## Description

This repository contains Python-based scrapers for extracting product listings and detailed product information from Tokopedia. These scrapers leverage the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) to handle JavaScript rendering, CAPTCHA challenges, and anti-bot protections. The extracted data is processed using BeautifulSoup for HTML parsing and Pandas for structured storage.

➡ Read the full blog [here](https://crawlbase.com/blog/how-to-scrape-tokopedia-data/) to learn more.

## Scrapers Overview

### Tokopedia Product Listing Scraper

The Tokopedia Product Listing Scraper (`tokopedia_listing_scraper.py`) extracts:

- **Product Name**
- **Price**
- **Product URL**
- **Shop Name**

The scraper supports pagination, ensuring comprehensive data extraction. The extracted data is saved in a JSON file.

### Tokopedia Product Detail Scraper

The Tokopedia Product Detail Scraper (`tokopedia_product_scraper.py`) extracts detailed product information, including:

- **Product Name**
- **Store Name**
- **Full Description**
- **Price**
- **Images URL**

The extracted data is saved in a JSON file.

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
# Use python3 if required (for Linux/macOS)
python --version
```

Next, install the required dependencies:

```bash
pip install crawlbase beautifulsoup4
```

- **Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
- **BeautifulSoup** – Parses and extracts structured data from HTML.

## Running the Scrapers

### Get Your Crawlbase Access Token

1. Sign up for Crawlbase [here](https://crawlbase.com/signup) to get an API token.
2. Use the **JS token** for Tokopedia scraping, as the site uses JavaScript-rendered content.

### Update the Scraper with Your Token

Replace "`YOUR_CRAWLBASE_TOKEN`" in the script with your Crawlbase JS Token.

### Run the Scraper

```bash
# For product listing scraping
python tokopedia_listing_scraper.py

# For product detail scraping
python tokopedia_product_scraper.py
```

The scraped data will be saved in `tokopedia_search_results.json` or `tokopedia_product_data.json`, depending on the script used.

## To-Do List

- Expand scrapers to extract additional product details like **discounted prices, seller reputation, and available promotions**.
- Optimize data storage and add support for **CSV and database integration**.
- Implement **asynchronous requests** to speed up data extraction.
- Enhance scraper efficiency with **Crawlbase Smart Proxy** to prevent blocks.
- Automate scheduled scraping for **real-time price monitoring and product tracking**.

## Why Use This Scraper?

- ✔ **Bypasses anti-bot protections** with Crawlbase.
- ✔ **Handles JavaScript-rendered content** seamlessly.
- ✔ **Extracts accurate and structured product dat**a efficiently.
