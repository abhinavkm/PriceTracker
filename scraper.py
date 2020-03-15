import requests 
from bs4 import BeautifulSoup

# url = 'https://smile.amazon.com/gp/product/B00ZSGVNH0/ref=ox_sc_saved_title_1?smid=A34TGPDNXFL7ZQ&psc=1'
URL = 'https://www.amazon.com/gp/product/B00ZSGVNH0/ref=ox_sc_saved_title_1?smid=A34TGPDNXFL7ZQ&psc=1'

header = {"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
page = requests.get(URL, headers=header)

# soup = BeautifulSoup(page.content, 'html.parser')

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title = soup2.find(id = "productTitle").get_text()
price = soup2.find(id = "priceblock_ourprice").get_text()
print(title.strip())
print(price.strip())

