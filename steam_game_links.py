# import BeautifulSoup from bs4 library
from bs4 import BeautifulSoup
# import url handling module
import urllib.request, urllib.parse, urllib.error

# Empty list to handle unfiltered links
links = list()
  
# URL for web scrape
# Can be changed
myurl = "https://store.steampowered.com/search/?sort_by=_ASC&ignore_preferences=1&specials=1&filter=topsellers"

# Putting every element of the page into variable html
html = urllib.request.urlopen(myurl).read()
# Parsing the html into variable soup
soup = BeautifulSoup(html, "html.parser")

# Search for every elemt under <a> tag
tags = soup("a")
for tag in tags:
    links.append(tag.get("href", None)) # Obtaining the links and putting into list links

# Creating function to filter links
def steamlink(links):
    if "store" and "app" in links:
        return True
    elif "store" and "bundle" in links:
        return True
    else:
        return False

# Applying filter towards links
filteredlinks = filter(steamlink, links)

# Printing filteredlinks
for link in filteredlinks:
    print(link)
