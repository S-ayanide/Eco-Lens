import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.ebay.com/')

soup = BeautifulSoup(r.text, 'html.parser')

resultsRow = soup.find_all('a', {'class': 'hl-item__link'})

results = []

for resultRow in resultsRow:
    itemURL = resultRow.get('href')    
    itemDesc = resultRow.select('img')[0].get('alt')    

    # Once formatted, the data are then appended to the results list
    results.append({
        'itemURL': itemURL,
        'itemDesc': itemDesc        
    })

print(results)