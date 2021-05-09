from django import forms
import re
from datetime import datetime, date
from .models import ContactDetailsTable


class HomeForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())

    # def clean(self):
    #     super().clean()
    #     self.add_error("username","username is mandatory")
    #     return self.cleaned_data

    # def clean(self):
    #     super().clean()
    #     for field, value in self.cleaned_data.copy().items():
    #         is_valid, error_msg = self.validate(field, value)
    #         if not is_valid:
    #             self.add_error(field, error_msg)
    #     return self.cleaned_data
    #
    # def validate(self,x,y):
    #
    #     print(x,y)
    #     return x,y


class ContactDetails(forms.Form):
    # HOW_DID_YOU_HEAR_CHOICES = [("None", "--None--"),
    #                             ("internet", "Internet"),
    #                             ("friend/relative", "Friend/Relative"),
    #                             ("socialnetworking", "Social Networking"),
    #                             ("advertisement", "Advertisement")]

    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField(required=True)
    project = forms.CharField(max_length=100, help_text='ex., Birthday, Marriage, House Warming')
    date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y'))
    #     input_formats=('%m/%d/%Y', ))
    # date = forms.DateField()
    venue = forms.CharField(max_length=100)
    budget = forms.IntegerField(required=True)
    guests = forms.IntegerField(required=True)
    aboutme = forms.CharField(widget=forms.Select(choices=ContactDetailsTable.HOW_DID_YOU_HEAR_CHOICES))
    questions = forms.CharField(max_length=2000, widget=forms.Textarea, required=False)

    def clean(self):
        super().clean()
        for field, value in self.cleaned_data.copy().items():
            print(type(field))
            print(field, value)
            is_error, error_msg = validate(field, value)
            # print(field, value, is_error, error_msg)
            if not is_error:
                self.add_error(field, error_msg)
                # print(self.cleaned_data)
        return self.cleaned_data


def validate(field, value):
    if field == 'firstname':
        if not value.isalpha():
            return False, 'Please enter a valid First Name'
    elif field == 'lastname':
        if not value.isalpha():
            return False, 'Please enter a valid Last Name'
    elif field == 'email':
        if not re.findall(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value):
            return False, 'Please enter a valid Email'
    elif field == 'phone':
        if not re.findall(r"(^\(?([0-9]{3})\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$)", str(value)):
            return False, 'Please enter a valid Phone Number'
    elif field == 'date':
        if datetime.strptime(str(value), '%Y-%m-%d').date() <= date.today():
            return False, 'Please enter a date greater than Today'
    return True, value



    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # phone = forms.IntegerField()
    # project_type = forms.CharField(max_length=100, label="Mention events like Birthdays, Maternity..")
    # date = forms.DateField()
    # venue = forms.CharField(max_length=100, label="Location")
    # budget = forms.IntegerField(label="In CAD")
    # guests_count = forms.IntegerField()
    # # how_did_you_hear = forms.ChoiceField(max_length=20, choices=HOW_DID_YOU_HEAR_CHOICES)
    # questions = forms.CharField(max_length=250, label="Any general or specific questions to me?")


# class QuoteForm(forms.Form):
#     dropdown = [
#         (None, "--None--"),
#         ("broadcast", "Broadcast"),
#         ("commercial", "Commercial"),
#         ("corporate video", "Corporate Video"),
#         ("feature film", "Feature Film")
#     ]
#
#     dropdown_1 = [
#         ("0", "Yes"),
#         ("1", "No"),
#         ("2", "Maybe")
#     ]
#
#     selection1 = forms.ChoiceField(choices=dropdown)
#     date = forms.CharField(label='Date(YYYY/MM/DD)', max_length=15)
#     availability = forms.ChoiceField(choices=dropdown_1)
