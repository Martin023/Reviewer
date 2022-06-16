from .models import *
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from review.forms import WebReviewForm

# Create your views here.
def home(request):
    projects = WebReview.display_site()
    highest_rating = 7
    return render(request,'home.html',{'highest_rating ':highest_rating, 'projects':projects})



def post_proj(request):
   
    if request.method == 'POST':
        form = WebReviewForm
        if form.is_valid:
            name = request.POST.get('name')
            description = request.POST.get('description')
            screenshot = request.POST.get('screenshot')
            category = request.POST.get('category')
            
            # messages.success("successfully submitted for review")
            new_site = WebReview(name,description,screenshot,category)
            new_site.save_site()

    form = WebReviewForm()
    return render(request,"post_project.html", {'form':form})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        f_name = request.POST.get('first_name')

        ## Or use f_name = request.POST['f_name']

        l_name = request.POST.get('last_name')

        email = request.POST.get('email')

        password = request.POST.get('password')

        c_password = request.POST.get('confirm_password')

        if password == c_password:
            my_user = User.objects.create_user(username,password,email)
            my_user.first_name = f_name
            my_user.last_name = l_name

            my_user.save()

            messages.success(request,"Account successfully created please login")

            return redirect("signin")

        else:
            messages.error(request,"Passwords don't match")

    return render(request,'register.html')

    
    