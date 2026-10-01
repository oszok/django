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