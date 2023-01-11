from django.shortcuts import render ,redirect
from django.contrib import messages
from django.core.paginator import Paginator 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from svg2font.models import Users
from .forms import UserForm
@login_required
def home(request):
    return HttpResponse("index.html")
@login_required
def about_us(request):
    return HttpResponse("about_us.html")

@login_required
def contact_us(request):
    return HttpResponse("contact_us.html")

@login_required
def svg2font(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid(): 
            form.save(commit=False).manager = request.user
            form.save()
            messages.success(request,("New User Added!"))
            return redirect('svg2font')
    else:
        all_users = Users.objects.filter(manager = request.user)
        paginator = Paginator(all_users, 5)
        page = request.GET.get("page")
        all_users = paginator.get_page(page)
        
        return render(request,'index.html',{'all_users':all_users})

def delete_user(request,user_id):
    delete_user_ = Users.objects.get(pk=user_id)
    if delete_user_.manager == request.user:
        delete_user_.delete()
        return redirect('svg2font')
    else:
        messages.error(request,("Access Restricted, You Are Not Allowed."))

    return redirect('svg2font') 
    
def user_edit(request,user_id):
    if request.method == "POST":
        edit_user_ = Users.objects.get(pk=user_id)
        edit_form = UserForm(request.POST or None, instance= edit_user_)
        if edit_form.is_valid(): 
            edit_form.save()
            messages.success(request,("User Edit Successfull"))
            return redirect('svg2font')
    else:
        user_obj_ = Users.objects.get(pk=user_id)
        return render(request,'edit.html',{'all_users':user_obj_})

def user_activaty(request,user_id):
    user_ = Users.objects.get(pk=user_id)
    if user_.manager == request.user:
        if user_.done == False:
            user_.done = True
            user_.save()    
            return redirect('svg2font')
        elif user_.done == True:
            user_.done = False
            user_.save()
            return redirect('svg2font')
    else:
        messages.error(request,("Access Restricted, You Are Not Allowed."))

    return redirect('svg2font')    
@login_required
def index(request):
    all_uesers = Users.objects.all
    return render(request,'index.html',{'all_users':all_uesers} )

# def manage(request):
#     return render(request,'manage.html',{})