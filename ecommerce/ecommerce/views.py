from django.shortcuts import render


def Header(request):
    return render(request, "header.html")
def About(request):
    return render(request, "about.html")
def Contact(request):
    return render(request, "contact.html")
def Index(request):
    return render(request, "index.html")
def Product(request):
    return render(request, "products.html")
def SingleProduct(request):
    return render(request, "single-product.html")