from django.shortcuts import render
from contact.models import Contacts
from django.http import HttpResponse

# Create your views here.
def SaveContact(request):
    print(request.POST.items)
    email = request.POST['email']
    name = request.POST['name']
    message = request.POST['message']

    Contacts.objects.create(email=email,name=name,message=message)
    return HttpResponse("your message has been saved", email)


def Contact(request):
    return render(request,"contact.html")
