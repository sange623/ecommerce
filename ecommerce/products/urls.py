from django.urls import path
from products import views

urlpatterns = [
    path('product-form/', views.ProductForm,name='product_form'),
    path('add-product/', views.SaveProduct,name='save_product'),
    path('add-category/', views.SaveCategory,name='save_category')

]
