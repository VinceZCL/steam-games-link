from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

links = list()
gamelinks = list()
  
myurl = "https://store.steampowered.com/search/?sort_by=_ASC&ignore_preferences=1&specials=1&filter=topsellers"

html = urllib.request.urlopen(myurl).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
for tag in tags:
    links.append(tag.get("href", None))

def steamlink(links):
    if "store" and "app" in links:
        return True
    elif "store" and "bundle" in links:
        return True
    else:
        return False

filteredlinks = filter(steamlink, links)
for a in filteredlinks:
    print(a)