from django.shortcuts import render
from django.http import HttpResponse
from home.forms import HomeForm

# Create your views here.


def home_page(request):
    return HttpResponse("New Home Page")


def new_home_page(request):
    return render(request, "base.html")


def home_form(request):
    form = HomeForm()

    if request.method == "GET":
        print("get method")

    if request.method == "POST":
        print("post method")
       # if form is valid and we should move the customer to the next page
        if form.is_valid():
            # :TODO add a entry into the table
            return HttpResponse("Successfully registered")

    # print("$", form.cleaned_data, "$")
    return render(request,"homeform.html", {'formkey': form})
