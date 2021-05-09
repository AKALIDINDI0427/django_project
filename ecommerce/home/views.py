from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.views import View

from .forms import ContactDetails, HomeForm
from .models import ContactDetailsTable
from ecommerce import settings

# Create your views here.
from .models import QuoteDetails


# def home_page(request):
#     return HttpResponse("New Home Page")
#
#
# def new_home_page(request):
#     return render(request, "base.html")
#

# class HomePage(View):
#     def get(self, request, *args, **kwargs):

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


# class HForm(View):
#
#     def get(self,request, *args, **kwargs):
#         form = HomeForm()
#         return render(request, "homeform.html", {"formkey":form})
#
#     def post(self, request, *args, **kwargs):
#         newform = HomeForm(request.POST)
#         if newform.is_valid():
#             return HttpResponse("Successfully registered")
#         return render(request, "homeform.html", {"fromkey":newform})
#
# class QForm(View):
#
#     def get(self,request, *args, **kwargs):
#         form = QuoteForm()
#         return render(request,"temp_quote.html",{"quoteform": form})
#
#     def post(self, request, *args, **kwargs):
#         newform = QuoteForm(request.POST)
#         if newform.is_valid():
#             # TODO: Will have save the date before sending success response
#             QuoteDetails.objects.create(project_type=newform.cleaned_data.get("selection1"), availability=newform.cleaned_data.get("availability"), date=newform.cleaned_data.get("date"))
#             print(newform.cleaned_data)
#             # import ipdb
#             # ipdb.set_trace()
#             return HttpResponse("Successfully Created a Quote")
#         print(newform)
#         return render(request,"temp_quote.html", {"fromkey":newform})
#
#     # def Quote(request):
#     #     return render(request,"temp_quote.html",{"quoteform": QuoteForm()})
#
#
# def Calendar(request):
#     return HttpResponse("This is Calendar page")
#
#
# def Sale(request):
#     return HttpResponse("This is Sales page")
#
#
# def ContactUs(request):
#     return HttpResponse("This is Contact Us page")
#
#
# def Testimonials(request):
#     return HttpResponse("This is Testimonials page")

# class HomePage(View):
#     def get(self, request, *args, **kwargs):
#         form = HomeForm()
#         return render(request,index.h)
#


def portfolio_page(request):
    return render(request, "index.html")


def about_page(request):
    return render(request, "about.html")


def thankyou_page(request):
    return render(request, "thankyou.html")
#
# def contactform(request):
#     return render(request, "contact.html")


# class Contact(View):
#
#     def get(self, request, *args, **kwargs):
#         form = ContactDetails()
#         return render(request, "contact.html", {'formkey': form})
#
#     def post(self, request, *args, **kwargs):
#         form = ContactDetails(request.POST)
#         if form.is_valid():
#             return HttpResponse("Successfully registered")
#         return render(request, "contact.html", {"formkey": form})


# class ContactPage(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'contact.html')
#
#     def post(self, request, *args, **kwargs):
#         form = ContactDetails(request.POST)
#         if form.is_valid():
#             return redirect('contact')
#         return render(request, 'contact.html', {'form': form})


class ContactPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')

    def post(self, request, *args, **kwargs):
        form = ContactDetails(request.POST)
        if form.is_valid():
            data = ContactDetailsTable.objects.create(firstname=form.cleaned_data.get('firstname'),
                                               lastname=form.cleaned_data.get('lastname'),
                                               email=form.cleaned_data.get('email'),
                                               phone=form.cleaned_data.get('phone'),
                                               project=form.cleaned_data.get('project'),
                                               date=form.cleaned_data.get('date'),
                                               venue=form.cleaned_data.get('venue'),
                                               budget=form.cleaned_data.get('budget'),
                                               guests=form.cleaned_data.get('guests'),
                                               aboutme=form.cleaned_data.get('aboutme'),
                                               questions=form.cleaned_data.get('questions'))
            data.save()
            subject = 'AJ Photography - Thank you for reaching to us'
            message = F"""Hello {form.cleaned_data.get('firstname')},
                        
                        Thank you for reaching to us. It means a world to us :). 
                        We will soon respond to you with a confirmation.
                        
                        You have provided below details. Please let us know for any changes.
                        Name: {form.cleaned_data.get('firstname')}
                        Phone: {form.cleaned_data.get('phone')}
                        Project: {form.cleaned_data.get('project')}
                        Date: {form.cleaned_data.get('date')}
                        Venue: {form.cleaned_data.get('venue')}
                        Budget: {form.cleaned_data.get('budget')}
                        Guests: {form.cleaned_data.get('guests')}
                        Questions: {form.cleaned_data.get('questions')}
                         
                         
                Thank you!
                    """
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [form.cleaned_data.get('email'), settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid Header found')
            # return redirect('contact')
            return HttpResponseRedirect('ThankYou/')
        return render(request, 'contact.html', {'form': form})

