import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/Razer-Mamba-Wireless-Programmable-Gaming/dp/B07GBYYSMF/ref=sr_1_2_sspa?crid=ZNYKVPAFRGWT&keywords=razer+wireless+mouse&qid=1567444512&s=gateway&sprefix=razer+w%2Caps%2C180&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMkZYVFlKM0VQMEJUJmVuY3J5cHRlZElkPUEwNDU0MTQwMlBIVlpUNFNGQzRURCZlbmNyeXB0ZWRBZElkPUEwMjkzNjExMkxPWDJNV1FPTE9PWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])

    if(converted_price < 80.0):
        send_mail(title)

def send_mail(title):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('kyahata.america@gmail.com', 'gljdnscakjmdgpux')

    subject = f"Price fell down! {title}"
    body = 'Check the amazon link https://www.amazon.com/Razer-Mamba-Wireless-Programmable-Gaming/dp/B07GBYYSMF/ref=sr_1_2_sspa?crid=ZNYKVPAFRGWT&keywords=razer+wireless+mouse&qid=1567444512&s=gateway&sprefix=razer+w%2Caps%2C180&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMkZYVFlKM0VQMEJUJmVuY3J5cHRlZElkPUEwNDU0MTQwMlBIVlpUNFNGQzRURCZlbmNyeXB0ZWRBZElkPUEwMjkzNjExMkxPWDJNV1FPTE9PWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'kyahata.america@gmail.com',
        'k.yahata1610168@gmail.com',
        msg
    )
    print('EMAIL HAS BEEN SENT!')

    server.quit()

while True:
    check_price()
    time.sleep(60 * 60)

