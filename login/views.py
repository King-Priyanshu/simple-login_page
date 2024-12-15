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

        try:
            user = User.objects.get(email=email)
            pop={
                'note': 'email alrady exist'
            }
            return render(request, 'signup.html',pop)

        except :
             user = User(username=username, email=email, password=password)   
             user.save()
             return render(request,'login.html')
        





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


                    
                    
