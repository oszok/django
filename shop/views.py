from django.http import Http404
from django.shortcuts import redirect, render
from .forms import ProductForm, SearchForm

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 2999, "category": "laptops", "is_available": True},
    {"id": 2, "name": "Mysz", "price": 49, "category": "accessories", "is_available": False},
    {"id": 3, "name": "Klawiatura", "price": 199, "category": "accessories", "is_available": True},
    {"id": 4, "name": "Monitor", "price": 899, "category": "monitors", "is_available": True},
    {"id": 5, "name": "Słuchawki", "price": 149, "category": "accessories", "is_available": False},
]


def product_list(request):
    form = SearchForm(request.GET)
    products = PRODUCTS
    if form.is_valid():
        q = form.cleaned_data["q"]
        if q:
            products = [p for p in products if q.lower() in p["name"].lower()]
        if form.cleaned_data["only_available"]:
            products = [p for p in products if p["is_available"]]
    return render(request, "shop/product_list.html", {"products": products, "form": form})


def product_detail(request, product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product is None:
        raise Http404("Nie ma takiego produktu")
    return render(request, "shop/product_detail.html", {"product": product})

def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            PRODUCTS.append({"id": len(PRODUCTS) + 1, **data})
            return redirect("shop:product_list")
    else:
        form = ProductForm()
    return render(request, "shop/product_form.html", {"form": form})




# Biernat


