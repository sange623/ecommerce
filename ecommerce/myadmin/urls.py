from django.urls import path
from .import views
urlpatterns = [
    path('login/', views.Login,name='login'),
    path('admin-index/', views.Index,name='admin-index'),
    path('accounts/', views.Account,name='admin-account'),
    path('add-product/', views.AddProduct,name='admin-addproduct'),
    path('edit-product/', views.EditProduct,name='editProduct'),
    path('products/', views.Products,name='admin-products'),
    path('admin-logout/', views.Logout,name='admin-logout'),
    path('admin-category/', views.Categories,name='admin-category'),
]
