import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
city="karachi"
product="samsung-s7/"
cat="mobile-phones"
url="https://www.olx.com.pk/{}/{}/q-{}/".format(city,cat,product)
# url="https://www.olx.com.pk/{}/q-{}".format(city,product)
# url="http://quotes.toscrape.com"
sleep(10)
data = requests.get(url)
soup=BeautifulSoup(data.text,"html.parser")

titles = soup.find_all(class_="lpv-item-info--description")
price = soup.find_all(class_="lpv-item-info--price")

with open("olx_scraped.txt","w") as file:
	for title in titles:
		file.write(title.find("h3").get_text())
with open("olx_scraped.txt","a") as file:
	file.write("\n")
	file.write("Now prices")
	for pr in price:
		file.write(pr.get_text())

