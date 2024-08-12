from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import is_valid_path, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import FormView, CreateView, UpdateView, ListView, DetailView


from .models import User
# Create your views here.

class UserLoginFormView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff == True:
                login(request, user)
                response = redirect('index')
                return response
            login(request, user)
            response = redirect('index')
            return response
        else:
            response = redirect('login')
            return response

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")


class UserRegisterFormView(CreateView):

    def get(self, request):
        return render(request, 'registration.html')
    
    def post(self, request):
        new_user = User.objects.create(
            username=request.POST.get('username', ''),
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone_number', ''),
            address=request.POST.get('address', ''),
            birthday=request.POST.get('birthday', '')
        )
        password = request.POST.get('password', '')
        password1 = request.POST.get('password1', '')

        if password == password1:
            new_user.set_password(password)
            new_user.save()

        else:
            raise ValueError("error")
        user = authenticate(username=new_user.username, password=password1)
        
        if user is not None:
            login(request, user)
            response = redirect('index')
            return response
        else:
            return redirect('login')
        

class UserProfileView(DetailView):

    template_name = 'profile.html'
    model = User
    def get_object(self):
        return get_object_or_404(User, pk = self.request.user.id)