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
    

x = urlgen(31, "dinner")
c = x.replace('"', '')
URL = c
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")



def recepiegen():
    results = soup.find(id="mntl-sc-block_3-0")
    job_elements = str(results.find_all("p", class_="comp mntl-sc-block mntl-sc-block-html"))
    x = re.sub('<[^>]+>', '', job_elements)
    return x

def ingredientsgen():
    results = soup.find(id="section--ingredients_1-0")
    ingredients = str(results.find_all("span"))
    c = re.sub('<[^>]+>', '', ingredients)
    c1 = c.replace(",", "")
    c1.split()
    return c1
    
x = ingredientsgen()
y = recepiegen()

text_file = open("recipie.txt", "w")
 

text_file.write(x+y)

text_file.close()


