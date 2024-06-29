from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AddProducts, Category

# Create your views here.
def ProductForm(request):
    data = {
        "category" : Category.objects.all()
    }
    print(request.POST.items)
    return render(request,'dashboard/products.html',data)
def SaveCategory(request):
    category_name = request.POST['category_name']
    Category.objects.create(category=category_name)
    return redirect('admin-products')

def SaveProduct(request):
    print(request.POST.items)
    product_name = request.POST['name']
    description = request.POST['description']
    category_id = request.POST["category"]
    price = request.POST["price"]
    unit = request.POST["unit"]
    image = request.FILES["image"]
    category_instance = Category.objects.get(id=category_id)
    AddProducts.objects.create(product_name=product_name,description=description,category=category_instance,price=price,unit=unit,image=image)
    # return HttpResponse(product_name)
    return redirect('admin-products')


