import requests
from bs4 import BeautifulSoup
import json

from soupsieve import select

url = 'https://www.ceneo.pl/105186036#tab=reviews'
all_opinions = []

while(url):
    response = requests.get(url)
    page_code = BeautifulSoup(response.text, 'html.parser')
    opinions = page_code.select('div.js_product-review')

    for opinion in opinions:
        opinion_id =  opinion["data-entry-id"]
    
        opinion_author =  page_code.select_one('span.user-post__author-name').get_text().strip()
    
        try:
            recommendation =  opinion.select_one('em.recommended').get_text().strip()
        except AttributeError:
            recommendation = None
            
        stars =  opinion.select_one('span.user-post__score-count').get_text()

        opinion_text =  page_code.select_one('div.user-post__text').get_text().strip()

        defects = opinion.select("div[class$=negatives] ~ div.review-feature__item")
        defects = [item.get_text().strip() for item in defects]
    
        advantages = opinion.select("div[class$=positives] ~ div.review-feature__item")
        advantages = [item.get_text().strip() for item in advantages]
    
        useful =  opinion.select_one('button.vote-yes')["data-total-vote"]

        useless =  opinion.select_one('button.vote-no')["data-total-vote"]
    
        published_date =  opinion.select_one('span.user-post__published > time:nth-child(1)')["datetime"]

        try:
            purchased_date =  opinion.select_one('span.user-post__published > time:nth-child(2)')["datetime"]
        except TypeError:
            purchased_date = None
        
        single_opinion = {
            "id": opinion_id,
            "author": opinion_author,
            "recommendatio": recommendation,
            "stars": stars,
            "text": opinion_text,
            "defects": defects,
            "advantages": advantages,
            "useful": useful,
            "useless": useless,
            "published_date": published_date,
            "purchased_date": purchased_date,
        }
        all_opinions.append(single_opinion)

    try:
        url = 'https://www.ceneo.pl' + page_code.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None
            
with open("opinions/29042022.json", "w", encoding="UTF-8") as json_file:
    json.dump(all_opinions, json_file, indent=4, ensure_ascii=False)

