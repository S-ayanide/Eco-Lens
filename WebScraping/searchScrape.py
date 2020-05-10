import requests
import pickle
from bs4 import BeautifulSoup

# Loading Saved Dataset
with open('../Data/search_circle','rb') as item_data:
    search_circle_data = pickle.load(item_data)

item_url = [] # empty array to store all the item url lists

# Search Item
for item in search_circle_data:

    # Product Search Page [Can search further]
    search_item_url = requests.get(item['href'])
    soup = BeautifulSoup(search_item_url.text, 'html.parser')

    # Get all the urls of the scrollable items which expands further to searchable lists
    scroll_items = soup.find_all('a', {'class': 'b-guidancecard__link'})

    # Get urls of items to fetch Item Details
    item_detail = soup.find_all('a', {'class': 'b-tile'})
    product_overview = []

    # Getting individual url to expand the search further [Feature]
    for individual_item in scroll_items:
        product_url = individual_item.get('href')
    
    # Fetching the individual lists of urls for items to be explored for Parameters
    for individual_product in item_detail:
        product_detail_url = individual_product.get('href')

        # Storing the item url list into a JSON file using Pickle
        item_url.append({
            'item_url': product_detail_url
        })        

        with open('../Data/item_details_url','wb') as item_data:
            pickle.dump(item_url, item_data)