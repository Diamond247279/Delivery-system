from django.shortcuts import  render, redirect,reverse
from .forms import CustomUserForm
from django.contrib.auth import login
from django.contrib import messages
from .email_backend import EmailBackend

# Create your views here.
def homepage(request):
    context={
        'title':'HOMEPAGE'
    }
    return render(request, 'general/index.html',context)

def about(request):
    context={
        'title':'ABOUT US'
    }
    return render(request, 'general/about.html',context)

def services(request):
    context={
        'title':'SERVICES'
    }
    return render(request, 'general/services.html',context)

def price(request):
    context={
        'title':'PRICE'
    }
    return render(request, 'general/pricing.html',context)

def contact(request):
    context={
        'title':'CONTACT US'
    }
    return render(request, 'general/contact.html',context)

def quote(request):
    context={
        'title':'GET A QUOTE'
    }
    return render(request, 'general/get-a-quote.html',context)

def details(request):
    context={
        'title':'SERVICE DETAILS'
    }
    return render(request, 'general/service-details.html',context)
    
def sign_up(request):
    form=CustomUserForm(request.POST or None, request.FILES or None)
    context={
        'title':'SIGN UP',
        'form':form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'registration successful')
            return redirect(reverse('sign_in'))
        else:
            messages.error(request,'unsuccessful')	    
    return render(request, 'general/sign_up.html',context)

def sign_in(request):
    context={
        'title':'SIGN IN'
    }
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=EmailBackend.authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request, 'invalid credentials')
            return redirect(reverse('sign_in'))
        else:
            login(request,user)
            messages.success(request,'access granted')
            return redirect(reverse('dashboard'))
    return render(request,'general/sign_in.html',context)

def dashboard(request):
    return render(request,'general/dashboard.html')

def logout_page(request):
    logout(request)
    messages.info(request,'logged out')
    return redirect('sign_in')



