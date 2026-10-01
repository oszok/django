from django import forms

CATEGORIES = [
    ("laptops", "Laptopy"),
    ("accessories", "Akcesoria"),
    ("monitors", "Monitory"),
]


class ProductForm(forms.Form):
    name = forms.CharField(label="Nazwa", max_length=100, min_length=3)
    price = forms.DecimalField(label="Cena", min_value=0.01, max_digits=8, decimal_places=2)
    category = forms.ChoiceField(label="Kategoria", choices=CATEGORIES)
    is_available = forms.BooleanField(label="Dostępny", required=False, initial=True)
    description = forms.CharField(label="Opis", widget=forms.Textarea, required=False)

class SearchForm(forms.Form):
    q = forms.CharField(label="Szukaj", required=False, max_length=50)
    only_available = forms.BooleanField(label="Tylko dostępne", required=False)