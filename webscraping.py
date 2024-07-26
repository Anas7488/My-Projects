import requests
from bs4 import BeautifulSoup

# Target URL (replace with the actual website you want to scrape)
req = requests.get("https://www.amazon.com/")


soup = BeautifulSoup(req.content,"html.parser")

#res = soup.title

print(soup.get_text())
