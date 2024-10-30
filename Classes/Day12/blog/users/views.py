from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')  # Redirect to login after successful registration


def CustomLogout(request):
    if request.user.is_authenticated:
        logout(request)
    context = {'x':2}
    return render(request,'login.html',context)

    