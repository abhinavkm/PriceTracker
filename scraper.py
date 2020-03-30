import requests 
from bs4 import BeautifulSoup
import smtplib

# url = 'https://smile.amazon.com/gp/product/B00ZSGVNH0/ref=ox_sc_saved_title_1?smid=A34TGPDNXFL7ZQ&psc=1'
URL = 'https://www.amazon.com/gp/product/B00ZSGVNH0/ref=ox_sc_saved_title_1?smid=A34TGPDNXFL7ZQ&psc=1'

header = {"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

def check_price():    
    page = requests.get(URL, headers=header)

    # soup = BeautifulSoup(page.content, 'html.parser')

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id = "productTitle").get_text()
    price = float(soup2.find(id = "priceblock_ourprice").get_text()[1:])
    print(title.strip())
    print(price)

    if(price < 30.00):
        print("the price is right!")
        # send_mail()

# check_price()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # server.login('abhinav.abhi96@gmail.com', )
