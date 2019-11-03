##webscraping day2

## hosting html page using python
## python -m http.server 8080


## exploring xpath

## getting the html

import requests
from lxml import html

##fetching html
page_html  = requests.get("http://localhost:8080/planets.html")

#processing using html
tree = html.fromstring(page_html.text)


##selcting table and required table rows using xpath
trs = tree.xpath("/html/body/div/table/tr[@class='planet']")


##extracting data from selected rows
for tr in trs :
        name = tr.xpath("./td[2]/text()[1]")[0].strip()
        mass = tr.xpath("./td[3]/text()[1]")[0].strip()
        planet = dict()
        planet[name] = mass
        print(planet)
