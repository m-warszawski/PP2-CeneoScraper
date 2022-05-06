import requests
from bs4 import BeautifulSoup
import json


print("=== Witaj w Ceneo Scraper! ===")
id = input("Podaj ID produktu: ")
url = f'https://www.ceneo.pl/{id}#tab=reviews'


def get_item(ancestor, selector, attribute=None, return_list=False):
    try:
        if return_list:
            return [item.get_text().strip() for item in ancestor.select_one(selector)]
        if attribute:
            return ancestor.select_one(selector)[attribute]
        return ancestor.select_one(selector).get_text().strip()
    except (AttributeError, TypeError):
        return None

selectors = {
        'author': ['span.user-post__author-name'],
        'recommendation': ['em.recommended'],
        'stars': ['span.user-post__score-count'],
        'text': ['div.user-post__text'],
        'advantages': ['div[class$=positives] ~ div.review-feature__item', None, True],
        'defects': ['div[class$=negatives] ~ div.review-feature__item', None, True],
        'useful': ['button.vote-yes', 'data-total-vote'],
        'useless': ['button.vote-no', 'data-total-vote'],
        'published_date': ['span.user-post__published > time:nth-child(1)', 'datetime'],
        'purchased_date': ['span.user-post__published > time:nth-child(2)', 'datetime'],
}

all_opinions = []
opinions_count = 0
print("Wyszukiwanie...")

while(url):
    response = requests.get(url)
    page_code = BeautifulSoup(response.text, 'html.parser')
    opinions = page_code.select('div.js_product-review')

    for opinion in opinions:
        single_opinion = {
            key:get_item(opinion, *value)
                for key, value in selectors.items()
        }
        single_opinion["opinion_id"] =  opinion["data-entry-id"]
        all_opinions.append(single_opinion)
        opinions_count += 1

    try:
        url = 'https://www.ceneo.pl' + page_code.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None

print(f"Znaleziono {opinions_count} opinii")
print("Zapisywanie...")           
try:            
    with open(f"opinions/{id}.json", "w", encoding="UTF-8") as json_file:
        json.dump(all_opinions, json_file, indent=4, ensure_ascii=False)
    print(f"Zapisano do pliku :) ")
except:
    print("Napotkano błąd!")


