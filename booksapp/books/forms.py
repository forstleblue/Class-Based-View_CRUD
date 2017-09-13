from django import forms

class UpdateForm(forms.Form):
    isbn = forms.CharField(required=True)
    title = forms.CharField(required=True)
    publisher = forms.CharField(required=True)
    author = forms.CharField(required=True)
    pages = forms.CharField(required=True)





