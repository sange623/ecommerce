from django.shortcuts import render
from products.models import AddProducts,Category


def Header(request):
    return render(request, "header.html")
def About(request):
    return render(request, "about.html")
def Contact(request):
    return render(request, "contact.html")
def Index(request):
    product_men = AddProducts.objects.filter(category_id=1)
    product_women = AddProducts.objects.filter(category_id=2)
    product_kid = AddProducts.objects.filter(category_id=3)
    # categories_list = Category.objects.all()
    data = {
        'mens' : product_men,
        'womens' : product_women,
        'kids' : product_kid,
        # 'categories' : categories_list
    }
    return render(request, "index.html",data)
def Product(request):
    return render(request, "products.html")
def SingleProduct(request):
    return render(request, "single-product.html")