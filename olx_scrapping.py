import requests
from bs4 import BeautifulSoup
import csv
city="karachi"
product="samsung-s7/"
cat="mobile-phones"
url="https://www.olx.com.pk/{}/{}/q-{}/".format(city,cat,product)
# url="https://www.olx.com.pk/{}/q-{}".format(city,product)
# url="http://quotes.toscrape.com"
data = requests.get(url)
soup=BeautifulSoup(data.text,"html.parser")

titles = soup.find_all(class_="lpv-item-info--description")
# print(titles)

for title in titles:
	print(title.find("h3").get_text())
