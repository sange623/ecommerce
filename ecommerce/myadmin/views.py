from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import login,logout,authenticate
from products.models import AddProducts,Category
# from .forms import AddProductForm,CategoryForm

# Create your views here.
def Login(request):
    data = {
        'login_active' : 'active'
    }
    # login(request,user=user_name)
    if request.method == "GET":
        return render(request, "dashboard/login.html",data)
    elif request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        user_obj = authenticate(username = user_name, password = password)
        if user_obj:
            login(request, user=user_obj)
            return Index(request)
        else:
            return HttpResponse("Sorry your account is invalid.")
  
    # return HttpResponse("asdkjhakjh ajdsh")
    return render(request, "dashboard/login.html")

# @user_passes_test(lambda u: u.is_superuser)
@login_required
def Logout(request):
    logout(request)
    data = {
        'logout_active' : 'active'
    }
    return render(request, "dashboard/login.html",data)

# @user_passes_test(lambda u: u.is_superuser)
@login_required
def Index(request):
    data = {
        'index_active' : 'active'
    }
    return render(request,"dashboard/index.html",data)
    # return HttpResponse('this is admin file')
    
# @user_passes_test(lambda u: u.is_superuser)
@login_required
def Account(request):
    data = {
        'account_active' : 'active'
    }
    return render(request, "dashboard/accounts.html",data)

# @user_passes_test(lambda u: u.is_superuser)
@login_required
def AddProduct(request):
    categories_list = Category.objects.all()
    # if request.method == "POST":
    #     print('saveproduct')
    #     my_forms = AddProductForm(request.POST)
    #     my_forms.save()
    data = {
        'addproduct_active' : 'active',
        'categories' : categories_list
    }
    return render(request, "dashboard/add-product.html",data)

# @user_passes_test(lambda u: u.is_superuser)
@login_required
def EditProduct(request):
    data = {
        'editproduct_active' : 'active'
    }
    return render(request, "dashboard/edit-product.html",data)
# @user_passes_test(lambda u: u.is_superuser)
@login_required
def Products(request):
    product_list = AddProducts.objects.all()
    categories_list = Category.objects.all()
    data = {
        'product_active' : 'active',
        'products' : product_list,
        'categories' : categories_list
    }
    return render(request, "dashboard/products.html",data)

def Categories(request):
    data = {
        'category_active' : 'active'
    }
    return render(request, "dashboard/category.html",data)
