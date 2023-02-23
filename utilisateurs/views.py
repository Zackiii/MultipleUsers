from django.shortcuts import render
from django.shortcuts import redirect
from .models import Customer, Manager
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from .forms import CustomerSignUpForm, ManagerSignUpForm
from django.contrib.auth import login
User = get_user_model()


def index(request):
    return render(request, 'users/index.html')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class ManagerSignUpView(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
