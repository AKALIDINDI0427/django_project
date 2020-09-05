from django import forms


class HomeForm(forms.Form):
    username = forms.CharField(label='Your user name', max_length=100)
    password = forms.CharField(label='your password', max_length=100, widget=forms.PasswordInput())
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

class QuoteForm(forms.Form):
    dropdown = [
        (None, "--None--"),
        ("broadcast", "Broadcast"),
        ("commercial", "Commercial"),
        ("corporate video", "Corporate Video"),
        ("feature film", "Feature Film")
    ]

    dropdown_1 = [
        ("0", "Yes"),
        ("1", "No"),
        ("2", "Maybe")
    ]

    selection1 = forms.ChoiceField(choices=dropdown)
    date = forms.CharField(label='Date(YYYY/MM/DD)', max_length=15)
    availability = forms.ChoiceField(choices=dropdown_1)
