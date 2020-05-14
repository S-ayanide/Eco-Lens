import requests
import pickle
from bs4 import BeautifulSoup

# Loading Saved Dataset
with open('../Data/item_details_url','rb') as item_data:
    url = pickle.load(item_data)

# Getting Item URLs
for url in url:
    # Product Details Page
    item_url = requests.get(url['item_url'])
    soup = BeautifulSoup(item_url.text, 'html.parser')

    # Extracting individual Attribute Labels to check for Country, Distance and Materials
    item_attrs = soup.get('div', {'class': 'sh-loc active sel'})
    print(item_attrs)