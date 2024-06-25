import requests
from bs4 import BeautifulSoup
import json
import jsonpath_ng as jp
import ast

url = 'https://api.camptocamp.org/outings/1635187'
nb_sorties = 1
#url = url + str(nb_sorties)
response = requests.get(url)



if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.get_text(separator=' ', strip=True)
    json_object = json.loads(page_text)
    
    for i in range (nb_sorties) :
        mon_parsing_title = "$['documents'][" + str(i) + "]['locales'][0]['title']"
        title = jp.parse(mon_parsing_title)
        result_title = title.find(json_object)
        
        mon_parsing_document_ID = "$['documents'][" + str(i) + "]['document_id']"
        document_ID = jp.parse(mon_parsing_document_ID)
        result_document_ID = document_ID.find(json_object)
        
        mon_parsing_date = "$['documents'][" + str(i) + "]['date_end']"
        date = jp.parse(mon_parsing_date)
        result_date = date.find(json_object)
        
        mon_parsing_activite = "$['documents'][" + str(i) + "]['activities']"
        activite = jp.parse(mon_parsing_activite)
        result_activite = activite.find(json_object)
        
        mon_parsing_cotation = "$['documents'][" + str(i) + "]['weather']"
        cotation = jp.parse(mon_parsing_cotation)
        result_cotation = cotation.find(json_object)
        print("hello",i)
        
        print(result_title[0].value,";",result_document_ID[0].value,";",result_date[0].value,";"
              ,result_activite[0].value,";",result_cotation[0].value)
    
    
    #f = open('/Users/jb.marzolf/Downloads/raph/sortieC2C-api.txt','a')
    #f.write(page_text)
    #f.close()
    
else:
    print(f"Erreur {response.status_code}")