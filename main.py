import requests
from bs4 import BeautifulSoup
import re
def urlgen(num, meal):
    URL = "https://www.simplyrecipes.com/{}recipes-5090746".format(meal + "-")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    recipienum = num
    results = str(soup.find(id="mntl-card-list-items_2-0-{}".format(recipienum)))
    start = 'href='
    end = ' id="mntl-card-list-items_2-0'
    realresult = results.split(start)[1].split(end)[0]
    return(str(realresult))
x = urlgen(12, "lunch")
c = x.replace('"', '')
print(c)
URL = c
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="section--ingredients_1-0")
ingredients = str(results.find_all("span"))
c = re.sub('<[^>]+>', '', ingredients)
c1 = c.replace(",", "")
print(c1)

