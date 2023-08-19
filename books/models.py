from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()
    loan_type = models.IntegerField(choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')])
    
    def __str__(self):
     return self.name

class Customer(AbstractUser):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    REQUIRED_FIELDS=['age', 'city', 'name']

# class Loan(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     loan_date = models.DateField()
#     return_date = models.DateField()

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE) 
    loan_type = models.IntegerField(choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')])
    return_date = models.DateField()
    
    # return_date = models.DateField()
    # REQUIRED_FIELDS = []

    def __str__(self):
        return f"Loan for {self.customer.username} - {self.book.name}"
