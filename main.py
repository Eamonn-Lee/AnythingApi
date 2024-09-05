import requests
from bs4 import BeautifulSoup
import json
from BFS_search import find

def scrape_dict(url):
    rsp = requests.get(url)
    
    if rsp.status_code == 200:

        soup = BeautifulSoup(rsp.content, 'html.parser')
        
        data = {}
        curr_heading = None
        
        for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li']):

            if element.name.startswith('h'): #headings
                curr_heading = element.get_text(strip=True)
                data[curr_heading] = []

            elif element.name in ['p', 'li'] and curr_heading: #paragraphs, lists
                data[curr_heading].append(element.get_text(strip=True))

            elif element.name in ['ul', 'ol'] and curr_heading: #list items
                for li in element.find_all('li'):
                    data[curr_heading].append(li.get_text(strip=True))


        for key in data: 
            if len(data[key]) == 1: #single item to strsing
                data[key] = data[key][0]
        
        return data
    

    else:
        print(f"Failure: {rsp.status_code}")
        return None
    


url = "https://finance.yahoo.com/quote/NVDA/"
keyword = "PE" #2020[edit]

scrape = scrape_dict(url)

if scrape:
    pretty_data = json.dumps(scrape, indent=4)
    print(pretty_data)

    #cannot find a free ai api


    new_json = find(pretty_data, keyword)
    #print(new_json)
