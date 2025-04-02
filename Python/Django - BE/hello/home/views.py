from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact


# Create your views here.
def index(request):
    context = {
        "name": "Django",
        "age": 20,
        "address": "Hyderabad",
        "courses": ["python", "django", "flask"],
    }
    return render(request, "index.html", context)


def about(request):
    return HttpResponse("this is about page")


def services(request):
    return HttpResponse("this is services page")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        date = datetime.today()
        # Save in db
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=date)
        contact.save()
    return HttpResponse("this is contacts page")
