import requests
import bs4

url = requests.get("https://nationaltoday.com/what-is-today/")

#print(url.text)
soup = bs4.BeautifulSoup(url.text, "lxml")

hi = soup.select(".holiday-title")

print(hi)

for holiday in hi:
    print(holiday.txt)