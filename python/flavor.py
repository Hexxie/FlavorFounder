from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/get_flavors', methods=['GET'])
def get_flavors():

    product = request.args.get('product')

    if not product:
        return jsonify({"error": "No product provided"}), 400

    keywords = ["sweet", "sour", "bitter", "salty", "umami"]
    flavor_count = {key: 0 for key in keywords}

    search_product_url = f"https://cosylab.iiitd.edu.in/flavordb2/entities?entity={product}&category="
    print(search_product_url)
    response = requests.get(search_product_url)

    data = json.loads(response.json())
    if data:
        entity = data[0]["entity_id"]
        print(f"Entity ID: {entity}")

    url = f'https://cosylab.iiitd.edu.in/flavordb2/entity_details?id={entity}'
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #print(soup)
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    table = soup.find('table', {'id': 'molecules'})
    
    rows = table.find_all('tr')
    # print(rows)

    for row in rows:
        row_text = row.text.lower() 
        for keyword in keywords:
            flavor_count[keyword] += row_text.count(keyword)


    img_src = f"https://cosylab.iiitd.edu.in/flavordb2/static/entities_images/{entity}.jpg"

    product_name = soup.find('h1').get_text(strip=True)
    print(product_name)

    #search for wiki link
    wiki_link = ""
    for a_tag in soup.find_all('a', href=True):
        if "wikipedia.org" in a_tag['href']:
            wiki_link = a_tag['href']

    # Download the image of product
    img_response = requests.get(img_src)
    if img_response.status_code == 200:
        # Save it to the file
        image_path = os.path.join('../public', f'{product}.jpg')
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        with open(image_path, 'wb') as file:
            file.write(img_response.content)
        return jsonify({
            "product_name": product_name,
            "flavor_count": flavor_count,
            "image_path": f'https://cosylab.iiitd.edu.in/flavordb2/static/entities_images/{entity}.jpg',
            "wiki_link": wiki_link
        })
    else:
        return jsonify({
                "product_name": product_name,
                "flavor_count": flavor_count,
                "image_path": "Image not found",
                "wiki_link": wiki_link
        })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)