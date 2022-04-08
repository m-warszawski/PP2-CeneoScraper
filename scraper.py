import requests
from bs4 import BeautifulSoup

url = 'https://www.ceneo.pl/105186036#tab=reviews_scroll'
response = requests.get(url)

page_code = BeautifulSoup(response.text, 'html.parser')
# print(page_code)

# Wszystkie opinie
opinions = page_code.select('div.js_product-review')
opinion = opinions.pop(0)

# --Dla 1 opini
opinion_id =  opinion["data-entry-id"]

opinion_author =  page_code.select_one('span.user-post__author-name').get_text().strip()

recommendation =  opinion.select_one('em.recommended').get_text().strip()

stars =  opinion.select_one('span.user-post__score-count').get_text()

opinion_text =  page_code.select_one('div.user-post__text').get_text().strip()

# defects =  page_code.select('div[class$=negatives] ~ div.review-feature__item')

# advantages  =  page_code.select('div.review-feature__col:has(review-feature__title--positives) > .review-feature__item')

useful =  opinion.select_one('button.vote-yes')["data-total-vote"]

useless =  opinion.select_one('button.vote-no')["data-total-vote"]

published_date =  opinion.select_one('span.user-post__published > time:nth-child(1)')["datetime"]

purchased_date =  opinion.select_one('span.user-post__published > time:nth-child(2)')["datetime"]

print(opinion_id, opinion_author, recommendation, stars, opinion_text, useful, useless, published_date, purchased_date)


