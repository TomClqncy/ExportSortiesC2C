import requests
from bs4 import BeautifulSoup
import json
import jsonpath_ng as jp
import ast
import math

url = 'https://api.camptocamp.org/outings?'
nb_sorties = 30
response = requests.get(url)
f = open('/Users/jb.marzolf/Downloads/raph/sortieC2C-api.txt','a')
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
        
        mon_parsing_cotation = "$['documents'][" + str(i) + "]['global_rating']"
        cotation = jp.parse(mon_parsing_cotation)
        result_cotation = cotation.find(json_object)

        mon_parsing_cotation1 = "$['documents'][" + str(i) + "]['rock_free_rating']"
        cotation1 = jp.parse(mon_parsing_cotation1)
        result_cotation1 = cotation1.find(json_object)
        
        mon_parsing_cotation2 = "$['documents'][" + str(i) + "]['labande_global_rating']"
        cotation2 = jp.parse(mon_parsing_cotation2)
        result_cotation2 = cotation2.find(json_object)
        
        mon_parsing_cotation3 = "$['documents'][" + str(i) + "]['hiking_rating']"
        cotation3 = jp.parse(mon_parsing_cotation3)
        result_cotation3 = cotation3.find(json_object)
        
        mon_parsing_cotation4 = "$['documents'][" + str(i) + "]['ice_rating']"
        cotation4 = jp.parse(mon_parsing_cotation4)
        result_cotation4 = cotation4.find(json_object)
        
        mon_parsing_cotation5 = "$['documents'][" + str(i) + "]['ski_rating']"
        cotation5 = jp.parse(mon_parsing_cotation5)
        result_cotation5 = cotation5.find(json_object)
        
        mon_parsing_cotation6 = "$['documents'][" + str(i) + "]['snowshoe_rating']"
        cotation6 = jp.parse(mon_parsing_cotation6)
        result_cotation6 = cotation6.find(json_object)
        
        mon_parsing_cotation7 = "$['documents'][" + str(i) + "]['via_ferrata_rating']"
        cotation7 = jp.parse(mon_parsing_cotation7)
        result_cotation7 = cotation7.find(json_object)
        
        mon_parsing_cotation8 = "$['documents'][" + str(i) + "]['mtb_up_rating']"
        cotation8 = jp.parse(mon_parsing_cotation8)
        result_cotation8 = cotation8.find(json_object)
        
        mon_parsing_cotation9 = "$['documents'][" + str(i) + "]['mtb_down_rating']"
        cotation9 = jp.parse(mon_parsing_cotation9)
        result_cotation9 = cotation9.find(json_object)
        
        mon_parsing_geom = "$['documents'][" + str(i) + "]['geometry']['geom']"
        geom = jp.parse(mon_parsing_geom)
        result_geom= geom.find(json_object)
        result_geom_json = result_geom[0].value        
        result_geom_str = ''.join(result_geom[0].value)
        result_geom_json_2 = json.loads(result_geom_str)
        lat, long = result_geom_json_2['coordinates']
              
        lat = (lat * 180) / 20037508.34
        long = (long * 180) / 20037508.34
        long = (math.atan(math.pow(math.e, long * (math.pi / 180)))* 360 ) / math.pi -90
        
        act = str(result_activite[0].value)
        
        
        try : 
            Sortie_str = result_cotation[0].value,";",result_title[0].value,";",result_document_ID[0].value,";",result_date[0].value,";",result_activite[0].value,";", long ,";", lat ,"\n" 
        except IndexError:

            if act == "['skitouring']":
                Sortie_str = result_cotation2[0].value,"/",result_cotation5[0].value,";",result_title[0].value,";",result_document_ID[0].value,";",result_date[0].value,";",result_activite[0].value,";", long ,";", lat,"\n" 
                
            elif act == "['hiking']":
                Sortie_str = result_cotation3[0].value,";",result_title[0].value,";",result_document_ID[0].value,";",result_date[0].value,";",result_activite[0].value,";", long ,";", lat,"\n" 
                
            elif act == "['rock_climbing']":
                Sortie_str = result_cotation1[0].value,";",result_title[0].value,";",result_document_ID[0].value,";",result_date[0].value,";",result_activite[0].value,";", long ,";", lat,"\n" 
            
            elif act == "['ice_climbing']":
                Sortie_str = result_cotation4[0].value,";",result_title[0].value,";",result_document_ID[0].value,";",result_date[0].value,";",result_activite[0].value,";", long ,";", lat ,"\n"
            
            elif act == "['snowshoeing']":
                Sortie_str = result_cotation6[0].value,";",result_title[0].value,";",result_document_ID[0].value,";",result_date[0].value,";",result_activite[0].value,";", long ,";", lat,"\n" 
                
            elif act == "['via_ferrata']":
                Sortie_str = result_cotation7[0].value,";",result_title[0].value,";",result_document_ID[0].value,";",result_date[0].value,";",result_activite[0].value,";", long ,";", lat,"\n" 
                
            elif act == "['mountain_biking']":
                Sortie_str = result_cotation8[0].value,"/",result_cotation9[0].value,";",result_title[0].value,";",result_document_ID[0].value,";",result_date[0].value,";",result_activite[0].value,";", long ,";", lat,"\n" 
            
            else :
                Sortie_str = "Cotation non rensenseignée",";",result_title[0].value,";",result_document_ID[0].value,";",result_date[0].value,";",result_activite[0].value,";", long ,";", lat,"\n" 
            f.write(str(Sortie_str))
print("effectuer")
f.close()   
  