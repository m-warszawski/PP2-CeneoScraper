# PP2-CeneoScraper

## Struktura opinii w serwisie
| Składowa opinii           |  Selektor                                                  | Nazwa zmiennej  | Typ danych |
|-------------------------|----------------------------------------------------------|---------------|----------|
| Opinia                    | div.js_product-review                                      | opinion         |            |
| Identyfikator opinii      | data-entry-id                                              | opinion_id      |            |
| Autor opinii              | span.user-post__author-name                                | opinion_author  |            |
| Rekomendacja autora       | em.recommended                                             | recommendation  |            |
| Liczba gwiazdek           | span.user-post__score-count                                | stars           |            |
| Treść opinii              | div.user-post__text                                        | opinion_text    |            |
| Lista zalet               | div[class$=positives] ~ div.review-feature__item           | defects         |            |
| Lista wad                 | div[class$=negatives] ~ div.review-feature__item           | advantages      |            |
| Dla ilu osób przydatna    | button.vote-yes'['data-total-vote]                         | usefull         |            |
| Dla ilu osób nieprzydatna | button.vote-no'['data-total-vote']                         | useless         |            |
| Data wystawienia opinii   | span.user-post__published > time:nth-child(1)['datetime']  | published_date  |            |
| Data zakupu produktu      | span.user-post__published > time:nth-child(2)'['datetime'] | purchased_date  |            |

## Etepy pracy nad projektem
1. Pobranie elementów pojedynczej opinii do niezależnych zmiennych
2. Zapisanie wszystkich elementów pojedynczej opinii do jednej zmiennej \(słownik\)
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie ich do listy
4. Pobranie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku .json
5. Dodawanie możliwości podania id produktu przez użytkownika za pomocą klawiatury
6. Refatoryzacja (optymalizacja) kodu:
    a. utworzenie funkcji do pobierania składowych strony HTML
    b. utworzenie słownika opisującego strukturę opinii wraz z selektorami poszczególnych elementów
    c. zamiana instrukcji pobierających składowe opinii do pojedynczych zmiennych tworzących z nich słowniik na wyrażenie słownikowe \(dictionary comprehension\) tworzące słownik reprezentujący pojedynczą opinię na podstawie słownika selektorów
7. Analiza opinii o wybranym produkcie
    1. Wszytanie wszystkich opinii o wsazanm produkcie do obiektu DataFrame
    2. Wyliczenie podstawowych statystyk na podstawie opinii
        1. Liczba wszystkich opinii o produkcie
        2. Liczba opinii w których autor poadał listę zalet produktu
        3. Liczba opinii w których autor podał listę wad produktu
        4. Średnia ocen produktu
    3. Przygotowanie wykresów na podstawie zawartości opinii
        1. Udział poszczególnych rekomendacjii w ogólnej liczbie opinii
        2. Histogram częstości występowania poszczególnych ocen (liczba gwiazdek)
