from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

links = list()
prices = list()
names = list()
new_links = list()
old_prices = list()

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
for link in filteredlinks:
    new_links.append(link)

for num in range(1,len(new_links)):
    old_price = soup.select(f"#search_resultsRows > a:nth-child({num}) > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.responsive_secondrow")
    if old_price == []:
        continue
    else:
        old_price_str = old_price[0].text
        old_price_str = old_price_str.strip()
        old_prices.append(old_price_str)

"""
for num in range(1,len(new_links)):
    price = soup.select(f"#search_resultsRows > a:nth-child({num}) > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.discounted.responsive_secondrow")
    if price == []:
        continue
    else:
        price_str = price[0].text
        price_str = price_str.strip()
        prices.append(price_str)
"""

for num in range(1, len(new_links)):
    name = soup.select(f"#search_resultsRows > a:nth-child({num}) > div.responsive_search_name_combined > div.col.search_name.ellipsis")
    if name == []:
        continue
    else:
        name_str = name[0].text
        name_str = name_str.strip()
        names.append(name_str)

def searchgame(game):

    print(names[game])

    chosen_game = names[game]
    split = chosen_game.split(" ")
    first = split[0]
    last = split[len(split)-1]

    if len(split) > 2:
        second_to_last = split[len(split)-2]
    
    if len(split) > 2:
        for link in new_links:
            if first in link:
                if last in link:
                    if second_to_last in link:
                        print(link)
    else:
        for link in new_links:
            if first in link:
                if last in link:
                    print(link)

print("----------------------------------------------------------------------------------------------------------------")
for num in range(0,46):
    print("Game {}".format(num))
    print("Name: ")
    print(names[num])
    #print("Link: ")
    #print(new_links[num])
    print("Price: ")
    print(old_prices[num])
    #print("Prices: (Original Price - New Price)")
    #print(prices[num])
    print("----------------------------------------------------------------------------------------------------------------")

search = int(input("Any game you wish to obtain the link of? Game "))
searchgame(search)
