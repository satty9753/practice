import requests
from bs4 import BeautifulSoup

r_html = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
soup = BeautifulSoup(r_html.content, "html.parser")
data1 = soup.find_all("div", class_="dek")
for item in data1:
    print(item.text.encode("UTF-8"))
data2 = soup.select(".content-section")
for item in data2:
    print(item.text.encode("UTF-8"))