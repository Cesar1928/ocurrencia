from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm
from contact.forms import Contact1, ContactForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password']) # None
            if user is not None:
                if user.is_active:
                    login(request, user)
                    contact_form = ContactForm()
                    return render(request, 'contact/contact.html', {'form':contact_form})                                    
                else:
                    return HttpResponse('El usuario no esta activo')
            else:
                return render(request, 'account/logaga.html')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

def cerrarsesion(request):
    return render(request, 'account/logged_out.html')

def contraseñacorrecta(request):
    return render(request, 'account/logaga.html')

#@login_required
#def dashboard(request):
    #return render(request, 
     #             'account/dashboard.html')


#def register(request):
#    if request.method == 'POST':
#        user_form = UserRegistrationForm(request.POST)
#        if user_form.is_valid():
#            new_user = user_form.save(commit=False)
#            new_user.set_password(
#                user_form.cleaned_data['password']
#            )
#            new_user.save()
#            return render(request,
#                          'account/register_done.html',
#                          {'new_user':new_user})
#    else:
#        user_form = UserRegistrationForm()
#    return render(request, 
#                      'account/register.html',
#                      {'user_form': user_form})