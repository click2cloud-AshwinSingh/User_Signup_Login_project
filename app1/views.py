from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<h1>Welcome to Home Page</h1>')


def signup(request):
    if request.method == 'POST':
        username = request.POST('username')
        firstname = request.POST('first_name')
        lastname = request.POST('last_name')
        email = request.POST('email_id')
        password = request.POST('password')

        x = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
        x.save()

        return render(request, 'success.html')

    else:
        return render(request, 'signup.html')
