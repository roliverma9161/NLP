import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all headline titles
titles = soup.find_all("span", class_="titleline")
for i, title in enumerate(titles[:5], 1):
    print(f"{i}. {title.text}")