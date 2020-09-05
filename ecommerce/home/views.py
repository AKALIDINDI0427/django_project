from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import HomeForm, QuoteForm

# Create your views here.
from .models import QuoteDetails


def home_page(request):
    return HttpResponse("New Home Page")


def new_home_page(request):
    return render(request, "base.html")


# def home_form(request):
#
#     if request.method == "GET":
#         form = HomeForm()
#
#     if request.method == "POST":
#         print("post method")
#        # if form is valid and we should move the customer to the next page
#         form = HomeForm(request.POST)
#         if form.is_valid():
#             # :TODO add a entry into the table
#             return HttpResponse("Successfully registered")
#
#     # print("$", form.cleaned_data, "$")
#     return render(request,"simple.html", {'formkey': form})


class HForm(View):

    def get(self,request, *args, **kwargs):
        form = HomeForm()
        return render(request,"base.html",{"formkey":form})

    def post(self, request, *args, **kwargs):
        newform = HomeForm(request.POST)
        if newform.is_valid():
            return HttpResponse("Successfully registered")
        return render(request,"simple.html", {"fromkey":newform})

class QForm(View):

    def get(self,request, *args, **kwargs):
        form = QuoteForm()
        return render(request,"temp_quote.html",{"quoteform": form})

    def post(self, request, *args, **kwargs):
        newform = QuoteForm(request.POST)
        if newform.is_valid():
            # TODO: Will have save the date before sending success response
            QuoteDetails.objects.create(project_type=newform.cleaned_data.get("selection1"), availability=newform.cleaned_data.get("availability"), date=newform.cleaned_data.get("date"))
            print(newform.cleaned_data)
            # import ipdb
            # ipdb.set_trace()
            return HttpResponse("Successfully Created a Quote")
        print(newform)
        return render(request,"temp_quote.html", {"fromkey":newform})

    # def Quote(request):
    #     return render(request,"temp_quote.html",{"quoteform": QuoteForm()})


def Calendar(request):
    return HttpResponse("This is Calendar page")


def Sale(request):
    return HttpResponse("This is Sales page")


def ContactUs(request):
    return HttpResponse("This is Contact Us page")


def Testimonials(request):
    return HttpResponse("This is Testimonials page")

