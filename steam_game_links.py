# Import modules
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

# Creating list templates
links = list()
prices = list()
new_links = list()
names = list()

# URL for web scrape
# Changable
myurl = "https://store.steampowered.com/search/?sort_by=_ASC&ignore_preferences=1&specials=1&filter=topsellers"

# Creating request and obtaining HTML
html = urllib.request.urlopen(myurl).read()
soup = BeautifulSoup(html, "html.parser")

# Getting list of links on the URL
tags = soup("a")
for tag in tags:
    links.append(tag.get("href", None))

# Filter function
def steamlink(links):
    if "store" and "app" in links:
        return True
    elif "store" and "bundle" in links:
        return True
    else:
        return False

# Link filtering
filteredlinks = filter(steamlink, links)
for link in filteredlinks:
    new_links.append(link)

# Obtaining prices
for num in range(0,len(new_links)):
    price = soup.select(f"#search_resultsRows > a:nth-child({num}) > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.discounted.responsive_secondrow")
    if price == []:
        continue
    else:
        price_str = price[0].text
        price_str = price_str.strip()
        prices.append(price_str)

# Obtaining names
for num in range(0, len(new_links)):
    name = soup.select(f"#search_resultsRows > a:nth-child({num}) > div.responsive_search_name_combined > div.col.search_name.ellipsis")
    if name == []:
        continue
    else:
        name_str = name[0].text
        name_str = name_str.strip()
        names.append(name_str)

# Outputting all information
for num in range(0,24):
    print("Name: ")
    print(names[num])
    print("Link: ")
    print(new_links[num])
    print("Prices: (Original Price - New Price)")
    print(prices[num])
    print("----------------------------------------------------------------------------------------------------------------")
