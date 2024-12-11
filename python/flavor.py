from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import json
import os

app = Flask(__name__)
CORS(app)

class FlavorFetcher:
    BASE_URL = "https://cosylab.iiitd.edu.in/flavordb2"
    KEYWORDS = ["sweet", "sour", "bitter", "salty", "umami"]

    def __init__(self, product):
        self.product = product
        self.entity_id = None
        self.soup = None

    def fetch_entity_id(self):
        """Fetch the entity ID for the given product."""
        print("fetch_entity_id")
        search_url = f"{self.BASE_URL}/entities?entity={self.product}&category="
        response = requests.get(search_url)
        data = json.loads(response.json())
        if data:
            self.entity_id = data[0]["entity_id"]
        else:
            raise ValueError("Product not found")

    def fetch_product_details(self):
        """Fetch product details."""
        print("fetch_product_details")
        detail_url = f"{self.BASE_URL}/entity_details?id={self.entity_id}"
        response = requests.get(detail_url)
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def count_flavours(self):
        """Count flavours in molecules"""
        print("count_flavours")
        flavor_count = {key: 0 for key in self.KEYWORDS}
        table = self.soup.find('table', {'id': 'molecules'})
        if table:
            rows = table.find_all('tr')
            for row in rows:
                row_text = row.text.lower()
                for keyword in self.KEYWORDS:
                    flavor_count[keyword] += row_text.count(keyword)
        return flavor_count

    def extract_product_name(self):
        """Extract the product name."""
        print("extract_product_name")
        return self.soup.find('h1').get_text(strip=True) if self.soup.find('h1') else "Unknown"

    def extract_wikipedia_link(self):
        """Extract Wikipedia link."""
        print("extract_wikipedia_link")
        for a_tag in self.soup.find_all('a', href=True):
            if "wikipedia.org" in a_tag['href']:
                return a_tag['href']
        return None

    def fetch_image_link(self):
        print("fetch_image_link")
        """Download the product image."""
        return f"{self.BASE_URL}/static/entities_images/{self.entity_id}.jpg"

@app.route('/get_flavors', methods=['GET'])
def get_flavors():
    product = request.args.get('product')
    if not product:
        return jsonify({"error": "No product provided"}), 400

    try:
        fetcher = FlavorFetcher(product)
        fetcher.fetch_entity_id()
        fetcher.fetch_product_details()

        flavor_count = fetcher.count_flavours()
        product_name = fetcher.extract_product_name()
        wiki_link = fetcher.extract_wikipedia_link()
        image_path = fetcher.fetch_image_link()

        return jsonify({
            "product_name": product_name,
            "flavor_count": flavor_count,
            "image_path": image_path,
            "wiki_link": wiki_link
        })
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)