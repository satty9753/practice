import requests
from bs4 import BeautifulSoup

r_html = requests.get('http://www.nytimes.com/')
soup = BeautifulSoup(r_html.content, "html.parser")
lines = soup.find_all("h2",{"class": "story-heading"})
for line in lines:
    print(line.text.encode('UTF-8').strip())