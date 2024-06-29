from django.urls import path
from .import views

urlpatterns = [
    path('contact/', views.Contact,name='contact'),
    path('save-contact', views.SaveContact,name='savecontact')
]
