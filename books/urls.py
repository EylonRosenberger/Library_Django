from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# urlpatterns = [
#    path('', views.books)
   
# ]
# http://127.0.0.1:8000/books/
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    # path('add_book/', views.add_book, name='add_book'),
    path('all_books/', views.all_books, name='all_books'),
    path('find_book/', views.find_book, name='find_book'),
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),
    path('loan_book/', views.loan_book, name='loan_book'),
    path('return_book/', views.return_book, name='return_book'),
    path('all_loans/', views.all_loans, name='all_loans'),
    path('late_loans/', views.late_loans, name='late_loans'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('add_book_admin/', views.add_book_admin, name='add_book_admin')
    
    # Add more patterns as needed
]

