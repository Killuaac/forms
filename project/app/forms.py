from django import forms


class UserForm(forms.Form):
    name = forms.CharField(required=True, label='Имя',
                           widget=forms.TextInput(attrs={'class': 'myclass'}))
    age = forms.IntegerField(required=False)
    email = forms.EmailField(required=False,
                             widget=forms.EmailInput(attrs={'class': 'lool'}))
    required_css_class = 'myclass'
