Podczas przepisywania pliku `product_list.html` wprowadziłem 4 zmiany:
1. Zamiana `url_for('static', ...)` na `{% load static %}` oraz tag `{% static '...' %}`.
2. Zamiana zmiennej pętli `loop.index` na `forloop.counter`.
3. Zamiana generatora linków `url_for('product_detail', id=p.id)` na tag `{% url 'shop:product_detail' p.id %}`.
4. Zamiana filtra `round(2)` na `floatformat:2`.

Łącznie poprawek: 4.

## Testy walidacji formularza

![Błędy walidacji](form_errors.png)

![Błąd 403 CSRF](csrf_error.png)

Atak CSRF polega na skłonieniu zalogowanego użytkownika do otwarcia złośliwej strony, która potajemnie wysyła formularz do innej witryny z wykorzystaniem jego zapamiętanych ciasteczek.
Django broni przed tym, dołączając do każdego formularza unikalny, losowy token, który zna wyłącznie nasza aplikacja.
Serwer odrzuca żądania POST bez poprawnego tokena kodem 403 Forbidden, co uniemożliwia obcej stronie podszycie się pod użytkownika.


## Wyszukiwarka i brak tokena CSRF (GET vs POST)

W formularzu wyszukiwania użyliśmy metody `GET` i celowo nie dołączyliśmy tagu `{% csrf_token %}`.

Formularze typu `GET` służą wyłącznie do pobierania i filtrowania danych, nie wprowadzając żadnych zmian w bazie danych ani na serwerze (zgodnie z zasadą bezstanowości HTTP). Atak CSRF (Cross-Site Request Forgery) ma na celu wywołanie niepożądanej akcji zmieniającej stan konta użytkownika (np. edycja, usunięcie danych, wykonanie przelewu). Ponieważ zapytanie `GET` jest bezpieczne i czytelne (wszystkie parametry są widoczne bezpośrednio w adresie URL, co pozwala np. na zapisanie linku w zakładkach), token CSRF jest w nim niepotrzebny i niewykorzystywany przez Django.