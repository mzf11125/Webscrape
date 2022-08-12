import requests
import bs4

url = requests.get("https://www.msn.com/en-us/news/us/monkeypox-cases-in-each-state-california-new-york-declare-emergencies-as-outbreak-grows/ar-AA10eeF3#:~:text=Alabama%3A%2019%20Alaska%3A,2%20Arizona%3A%20102")

#print(url.text)
soup = bs4.BeautifulSoup(url.text, "lxml")

hi = soup.find_all("p")[37:88]
#print(hi)



for cases in hi:
    print(cases.text)

