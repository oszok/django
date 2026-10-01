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

class ProductForm(forms.Form):
    # Dodajemy widget z atrybutem class="wide"
    name = forms.CharField(
        label="Nazwa",
        max_length=100,
        min_length=3,
        widget=forms.TextInput(attrs={"class": "wide"})
    )
    price = forms.DecimalField(label="Cena", min_value=0.01, max_digits=8, decimal_places=2)

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        # Reguła domeny: nazwa nie może być słowem testowym
        if name.lower() in {"test", "asdf", "demo", "xxx"}:
            raise forms.ValidationError("Wpisz prawdziwą nazwę produktu, a nie słowo testowe.")
        return name

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        category = cleaned_data.get("category")

        # Reguła domeny: Laptop nie może kosztować mniej niż 500 zł
        if price is not None and category == "laptops" and price < 500:
            self.add_error("price", "Laptop nie może kosztować mniej niż 500 zł. Sprawdź cenę lub kategorię.")

        return cleaned_data