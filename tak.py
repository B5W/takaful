import requests
from bs4 import BeautifulSoup

user = input('[+] Enter User : ')

url = "https://takafulalarabia.com/Mobile/CouponsUsedDetails.html"

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.5",
"Connection": "keep-alive",
"Content-Length": "17",
"Content-Type": "application/x-www-form-urlencoded",
"Cookie": "PHPSESSID=64df0f25a33ab120a33b2984f9da0dc9; _gcl_au=1.1.347737840.1640360091; _ga_C93ELVZZ45=GS1.1.1640360090.1.0.1640360091.0; _ga=GA1.2.180335886.1640360091; _gid=GA1.2.543405662.1640360092; _dc_gtm_UA-205146533-1=1; _gat_gtag_UA_205146533_1=1",
"Host": "takafulalarabia.com",
"Origin": "https://takafulalarabia.com",
"Referer": "https://takafulalarabia.com/Mobile/CouponsUsed/Error.html",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    
}

data = {

'SearchID': user,

}

response = requests.request("post", url, data=data, headers=headers)

soup=BeautifulSoup(response.content, "lxml")


print(soup.text)

