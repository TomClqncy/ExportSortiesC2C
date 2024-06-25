import requests
from bs4 import BeautifulSoup
import json
import jsonpath_ng as jp

url = 'https://api.camptocamp.org/outings?limit=1'  
response = requests.get(url)

if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.get_text(separator=' ', strip=True)
    json_object = json.loads(page_text)
    title = jp.parse("$['documents'][0]['locales'][0]['title']")
    result = title.find(json_object)
    #print(result[0].value)
    print(result)
    
    
    #f = open('/Users/jb.marzolf/Downloads/raph/sortieC2C-api.txt','a')
    #f.write(page_text)
    #f.close()
    #print(json_object['documents'])
    
else:
    print(f"Erreur {response.status_code}")