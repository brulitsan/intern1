import requests
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serialiser import UserSerializer


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User(username=username, password=password, email=email)
            user.save()
            return redirect('page', pk=user.pk)

        return render(request, 'main/login.html')
    return render(request, 'main/login.html')


def success_view(request):
    return render(request, 'main/main_page.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def UserProfileView(request, user_pk):
    user = User.objects.get(pk=user_pk)
    response = requests.get('http://127.0.0.1:8000/user/page/<int:pk>')
    user_profiles = response.json()
    return render(request, 'main/main_page.html', {'user_profiles': user_profiles, 'user': user})


# class dispatchhistoryitemsview(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, pk, *args, **kwargs):
#         items = get_object_or_404(User, id=self.kwargs.get('pk'))
#         serializer = UserSerializer(items)
#         return Response(serializer.data)