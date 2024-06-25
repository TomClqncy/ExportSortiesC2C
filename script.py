import requests
import json

url = 'https://api.camptocamp.org/outings?limit=1'  
response = requests.get(url)

print('Hello World')
f = open('monFichier.txt',"x")


f.write("Hello World")
f.close
