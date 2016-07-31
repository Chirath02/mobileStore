from django.views.generic import DetailView, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import Mobile


class IndexView(ListView):
    model = Mobile


class MobileDetail(DetailView):
    model = Mobile
    template_name = 'mobile/mobile_details.html'


class AddMobileView(CreateView):
    model = Mobile
    fields = ['model_name', 'battery_capacity', 'quantity', 'back_cam', 'ram', 'price', 'img']


class SignupView(View):
    form_class = UserForm
    template_name = 'SignUp.html'


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})