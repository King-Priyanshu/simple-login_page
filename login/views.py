from django.shortcuts import render, redirect, reverse
from .models import User

# Signup page view
def signupPage(request):
    return render(request, "signup.html")

# Login page view
def loginPage(request):
    return render(request, "login.html")

# Signup logic
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Save the new user
        user = User(username=username, email=email, password=password)
        user.save()

        # Redirect to login page after signup
        return redirect(reverse('login.html'))  # Update with actual login view name


# Login logic
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email and password:
            try:
                user = User.objects.get(email=email)
                if user.password == password:
                    d = {
                        'email': user.email,
                        'username': user.username,
                    }
                    return render(request, 'home.html', d)
                else:
                    pop={
                    'note': 'Wrong Password'
                }
                    return render(request, 'login.html',pop)  # Password incorrect
            except User.DoesNotExist:
                pop={
                    'note': 'Email not found'
                }
                return render(request, 'login.html',pop)  # User does not exist


                    
                    
