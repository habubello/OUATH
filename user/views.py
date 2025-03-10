from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.views.generic import FormView

from user.forms import LoginForm, RegisterForm
from user.custom_token import account_activation_token
from user.models import User


def base(request):
    return render(request, 'tesst.html')


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                return render(request,'ecourses/blog.html')
            else:
                messages.error(request, 'Invalid login')

    return render(request, 'ecourses/login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('ecourses:index')



def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()

            messages.success(request, 'Registration successful. You can now log in.')
            return redirect(login_page)

    return render(request, 'ecourses/register.html', {'form': form})

class RegisterPage(FormView):
    template_name = 'ecourses/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('ecourses:login_page')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        send_mail(
            'Welcome to Ecourses',
            'You have successfully registered.',
            'lutfullaevickh@gmail.com',
            [user.email],
            fail_silently=False
        )

        login(self.request, user)
        return redirect(self.success_url)



