from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

from .models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User(username=username, password=password, email=email)
            user.save()
            return redirect('success')

        return render(request, 'main/login.html')

    return render(request, 'main/login.html')


def success_view(request):
    return render(request, 'main/success.html')

