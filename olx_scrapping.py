import requests
from bs4 import BeautifulSoup
import csv
city="karachi"
product="samsung-s7/"
url="https://www.olx.com.pk/{}/q-{}".format(city,product)
data = requests.get(url)
soup=BeautifulSoup(data.text,"html.parser")
with open("olx_scrapping.txt","w") as file:
	file.write(soup)

