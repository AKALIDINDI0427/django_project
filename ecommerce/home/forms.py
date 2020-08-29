from django import forms


class HomeForm(forms.Form):
    username = forms.CharField(label='Your user name', max_length=100)
    password = forms.CharField(label='your password', max_length=100)
    def clean(self):
        super().clean()
        return self.cleaned_data