from bs4 import BeautifulSoup
import requests
import smtplib
import os

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

userid= os.getenv("username")
userpass= os.getenv("password")

target_price= 6000

url="https://www.amazon.com/dp/B0DJFJFSZ5/ref=sspa_dk_detail_0?pd_rd_i=B0DJFJFSZ5&pd_rd_w=eSguZ&content-id=amzn1.sym.3bc66c0a-cc61-4816-aa2d-e53327eaddb6&pf_rd_p=3bc66c0a-cc61-4816-aa2d-e53327eaddb6&pf_rd_r=TF2S2J1BSTMHA83844KD&pd_rd_wg=M2UYc&pd_rd_r=758939e5-65ce-4dab-9673-ffde29aa8ea3&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1"
response= requests.get(url,headers=header)
a_webpage=response.text
soup= BeautifulSoup(a_webpage,"html.parser")

price=soup.find(name="span",class_="a-offscreen").getText()
price_without_currency=float(price.split(",")[1])

if price_without_currency <= target_price:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=userid,password=userpass)
        connection.sendmail(from_addr=userid,
                            to_addrs="your@gmail.com",
                            msg="Subject:Instant price drop.\n\n Hello ravi the price of hot pot is lower than your target price")
