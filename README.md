# PP2-CeneoScraper

## Struktura opinii w serwisie
|---------------------------|-----------------------------------------------------------------------------------|----------------------|-----------------|
|      Składowa opinii      |           Selektor                                                                |    Nazwa zmiennej    |    Typ danych   |
|---------------------------------------------------------------------------------------------------------------|----------------------|-----------------|
| Opinia                    | div.js_product-review                                                             |   opinion            |  
| Identyfikator opinii      | div.js_product-review\["data-entry-id"\]                                          |   opinion_id         | 
| Autor opinii              | span.user-post__author-name                                                       |   opinion_author     |
| Rekomendacja autora       | em.recommended                                                                    |   recommendation     |
| Liczba gwiazdek           | span.user-post__score-count                                                       |   stars      |
| Treść opinii              | div.user-post__text                                                               |   opinion_text       |    
| Lista zalet               | div.review-feature__col:has(review-feature__title--positives) > .review-feature__item    | defects       |
| Lista wad                 | div\[class$=negatives\] ~ div.review-feature__item                                |   advantages         |
| Dla ilu osób przydatna    | button.vote-yes\["data-total-vote"\]                                              |   usefull            |
| Dla ilu osób nieprzydatna | button.vote-no\["data-total-vote"\]                                               |   useless            |
| Data wystawienia opinii   | span.user-post__published > time:nth-child(1)\["datetime"\]                       |   published_date     |
| Data zakupu produktu      | span.user-post__published > time:nth-child(2)\["datetime"\]                       |   purchased_date     |
|---------------------------|-----------------------------------------------------------------------------------|----------------------|-----------------|
