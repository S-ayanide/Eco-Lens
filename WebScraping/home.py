import requests
import pickle
from bs4 import BeautifulSoup

# HomePage
home = requests.get('https://www.ebay.com/')

soup = BeautifulSoup(home.text, 'html.parser')

resultsRow = soup.find_all('a', {'class': 'hl-item__link'})
search_circle = soup.find_all('a', {'class': 'hl-popular-destinations-link'})

results = []
popularDestination = []

for resultRow in resultsRow:
    itemURL = resultRow.get('href')
    itemDesc = resultRow.select('img')[0].get('alt')

    # Once formatted, the data are then appended to the results list
    results.append({
        'itemURL': itemURL,
        'itemDesc': itemDesc
    })
    
    with open('../Data/homescreen_item_list','wb') as item_data:
        pickle.dump(results, item_data)

for search_circle in search_circle:

    # Getting all the Popular Destination items href
    popularItemHref = search_circle.get('href')
    popularDestination.append({
        'href': popularItemHref
    })

    with open('../Data/search_circle','wb') as item_data:
        pickle.dump(popularDestination, item_data)