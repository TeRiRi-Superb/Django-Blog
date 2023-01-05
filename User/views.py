from django.shortcuts import render
from django.views.generic import View


class LoginVew(View):
    def get(self, request):
        return render(request, 'User/login.html')


class RegisterVew(View):
    def get(self, request):
        return render(request, 'User/register.html')