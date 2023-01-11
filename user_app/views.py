from django.shortcuts import render ,redirect  
# from django.http import HttpResponse
from .forms import CusmtomRegisterForm
from django.contrib import messages

def register(request):

    if request.method == "POST":
        register_form = CusmtomRegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created"))
            return redirect("register")
    else:
        register_form = CusmtomRegisterForm()

    return render(request,'register.html',{'register_form':register_form})
