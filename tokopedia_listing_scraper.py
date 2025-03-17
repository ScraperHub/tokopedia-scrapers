from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({ 'token': 'YOUR_CRAWLBASE_TOKEN' })

def fetch_html(url):
    options = {
        'ajax_wait': 'true',
        'page_wait': '5000'
    }
    response = crawling_api.get(url, options)
    if response['headers']['pc_status'] == '200':
        return response['body'].decode('utf-8')
    else:
        print(f"Failed to fetch page. Status code: {response['headers']['pc_status']}")
        return None

def parse_search_listings(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    for product in soup.select('div[data-testid="divSRPContentProducts"] div.css-5wh65g'):
        name = product.select_one('span.OWkG6oHwAppMn1hIBsC3pQ\\=\\=').text.strip() if product.select_one('span.OWkG6oHwAppMn1hIBsC3pQ\\=\\=') else 'N/A'
        price = product.select_one('div.ELhJqP-Bfiud3i5eBR8NWg\\=\\=').text.strip() if product.select_one('div.ELhJqP-Bfiud3i5eBR8NWg\\=\\=') else 'N/A'
        store = product.select_one('span.X6c-fdwuofj6zGvLKVUaNQ\\=\\=').text.strip() if product.select_one('span.X6c-fdwuofj6zGvLKVUaNQ\\=\\=') else 'N/A'
        product_url = product.select_one('a.Nq8NlC5Hk9KgVBJzMYBUsg\\=\\=')['href'] if product.select_one('a.Nq8NlC5Hk9KgVBJzMYBUsg\\=\\=') else 'N/A'

        products.append({
            'name': name,
            'price': price,
            'store': store,
            'product_url': product_url
        })

    return products

def scrape_multiple_pages(base_url, max_pages):
    all_products = []

    for page in range(1, max_pages + 1):
        paginated_url = f"{base_url}&page={page}"
        html_content = fetch_html(paginated_url)

        if html_content:
            products = parse_search_listings(html_content)
            all_products.extend(products)
        else:
            break

    return all_products

def save_to_json(data, filename='tokopedia_search_results.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filename}")

# Scraping data from Tokopedia search listings
base_url = 'https://www.tokopedia.com/search?q=headset'
max_pages = 5  # Adjust the number of pages you want to scrape
search_results = scrape_multiple_pages(base_url, max_pages)

# Save results to a JSON file
save_to_json(search_results)