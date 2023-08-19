from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from datetime import datetime, timedelta
from django.http import HttpResponse
from .models import Customer


def books(request):
   return HttpResponse("Hello DJANGO library")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Customer, Loan
from .forms import BookForm, LoanForm

def home(request):
    return render(request, 'home.html')

def is_admin_or_superuser(user):
    return user.is_authenticated and (user.is_superuser or user.is_staff)

@login_required
def profile(request):
    return render(request, 'profile.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def add_book_admin(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Book "{Book.name}" added successfully!')
            return redirect('admin_panel')
    else:
        form = BookForm()
    return render(request, 'add_book_admin.html', {'form': form})

# Adding a new book
# @login_required
# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Book added successfully!')
#             return redirect('admin_panel')
#     else:
#         form = BookForm()
#     # return render(request, 'add_book.html', {'form': form})
#         return render(request, 'add_book_admin.html', {'form': form})

# Displaying all books
def all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})

# Finding a book by name
def find_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        books = Book.objects.filter(name__icontains=name)
    else:
        books = Book.objects.none()
    return render(request, 'find_book.html', {'books': books})

# Removing a book
@login_required
def remove_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('all_books')
    return render(request, 'remove_book.html', {'book': book})

# Loaning a book
@login_required 
def loan_book(request):
    print(request) # extract book object, customer object and loan object. 
    if request.method == 'POST':
        loan_form = LoanForm(request.POST)
        if form.is_valid():
            loan = loan_form.save(commit=False)
            # Set return date based on book type
            if loan.book.loan_type == 1:
                loan.return_date = timedelta(days=7)
            elif loan.book.loan_type == 2:
                loan.return_date = timedelta(days=10)
            else:
                loan.return_date = timedelta(days=14)
            loan.book.return_date = datetime.now() + loan.return_date
            loan.save()
            messages.success(request, f'Book was added successfully. Return date is: {loan.return_date}')
            # loan.return_date = datetime.now() + timedelta(days=loan.return_days)
            return redirect('all_loans') #('all_loans')
    else:
        form = LoanForm()
    return render(request, 'loan_book.html', {'form': form})

# Returning a book
@login_required
def return_book(request):
    # Implement returning logic here
    return redirect('all_loans')

# Displaying all loans
@login_required
def all_loans(request):
    loans = Loan.objects.all()
    return render(request, 'all_loans.html', {'loans': loans})

# Displaying late loans
@login_required
def late_loans(request):
    # Implement late loan logic here
    return render(request, 'late_loans.html', {'late_loans': late_loans})

# Customer registration
def register(request):
    # Implement customer registration logic here
    if request.method == 'GET':
      return render(request, 'register.html')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        name=request.POST['name']
        city=request.POST['city']
        age=request.POST['age']
        user=Customer(username=username, password=password,email=email, name=name,city=city,age=age)
        user.set_password(password)
        user.save()
        return redirect('login')

# Customer login
def login_user(request):
    # Implement customer login logic here
    if request.method == 'GET':
      return render(request, 'login.html')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=Customer.objects.get(username=username)
        except:
            return render(request, 'login.html', {'message': 'Username or Password incorrect'})
        user=authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'login.html', {'message': 'Username or Password incorrect'})
        login(request, user)
        return redirect('home')
        
# Customer logout
@login_required
def logout_user(request):
    # Implement customer logout logic here
    logout(request)
    return redirect('home')

# Customer profile and personalized features
@login_required
def profile(request):
    user = request.user
    # Implement profile and personalized logic here
    return render(request, 'profile.html', {'user': user})

def admin_panel(request):
    books = Book.objects.all()
    return render(request, 'admin_panel.html', {'books': books})
