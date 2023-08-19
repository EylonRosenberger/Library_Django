from django import forms
from .models import Book, Loan

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'year_published', 'loan_type']
# name = forms.CharField(label="Book Name: ")
# author = forms.CharField(label="Author Name: ")
# year_published = forms.CharField(label="Year Published: ")
# loan_type = forms.CharField(label="Loan Type: ")

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['customer', 'book']


# class Customer(forms.Form):
#     name = forms.CharField(label="Name: ")
#     city = forms.CharField(label="City: ")
#     age = forms.CharField(label="Age: ")