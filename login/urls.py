from django.contrib import admin
from django.urls import path
from . import views

app_name = 'login'  # Setting the namespace for the app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', views.signupPage, name="signupPage"),  # Route for the signup page
    path('login/', views.loginPage, name="loginPage"),  # Login page route
    path('signup/', views.signup, name="signup"),  # Handle signup form submission
    path('login/authenticate/', views.login, name="login"),  # Route for login form submission (renamed)
]
