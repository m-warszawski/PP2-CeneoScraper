# PP2-CeneoScraper

## Struktura opinii w serwisie
|---------------------------|-----------------------------------------------------------------------------------|----------------|------------|
|      Składowa opinii      |           Selektor                                                                | Nazwa zmiennej | Typ danych |
|---------------------------------------------------------------------------------------------------------------|----------------|------------|
| Opinia                    | div.js_product-review                                                             |
| Identyfikator opinii      | div.js_product-review\["data-entry-id"\]                                          |            
| Autor opinii              | span.user-post__author-name                                                       |     
| Rekomendacja autora       | em.recommended                                                                    |
| Liczba gwiazdek           | span.user-post__score-count                                                       |
| Treść opinii              | div.user-post__text                                                               |
| Lista zalet               | div.review-feature > .review-feature__col:nth-child(1) > .review-feature__item    |
| Lista wad                 | div.review-feature > .review-feature__col:nth-child(2) > .review-feature__item    |
| Dla ilu osób przydatna    | button.vote-yes\["data-total-vote"\]                                              |
| Dla ilu osób nieprzydatna | button.vote-no\["data-total-vote"\]                                               |
| Data wystawienia opinii   | span.user-post__published > time:nth-child(1)\["datetime"\]                       |
| Data zakupu produktu      | span.user-post__published > time:nth-child(2)\["datetime"\]                       |
|---------------------------|-----------------------------------------------------------------------------------|    