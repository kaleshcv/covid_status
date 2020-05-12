from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User, auth
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Postnew

# Create your views here.

def register(req):

    if req.method=='POST':
        first_name=req.POST['first_name']
        last_name = req.POST['last_name']
        username=req.POST['username']
        password1 = req.POST['password1']
        password2 = req.POST['password2']
        email = req.POST['email']


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(req,'Username already taken !')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(req,'Email already exist, Please Login or register with another Email')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password2,email=email,first_name=first_name, last_name=last_name)

                user.save(); # create and save user

                print('User created')
                return redirect('login')
        else:
            #print("not matching")
            messages.error(req, 'Password not matching')
            return redirect('register')

    else:
        template = loader.get_template('register.html')
        data={}
        res = template.render(data,req)
        return HttpResponse(res)

def login(req):

    if req.method=='POST':
        username = req.POST['username']
        password = req.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req,user)
            return redirect('profile')
        else:
            messages.error(req,'Invalid Credential')
            return redirect('login')

    else:
        return render(req,'login.html')

def logout(req):
    auth.logout(req)
    return redirect('/')

def profile(req):

    template = loader.get_template('profile.html')
    all_post = Postnew.objects.all().order_by('post_date').reverse()
    data = {'posts': all_post}
    res = template.render(data, req)
    return HttpResponse(res)

def addpost(req):

    if req.method == 'POST':
        post_title = req.POST['post_title']
        post_content = req.POST['post_content']
        post_owner = req.POST['post_owner']

        post=Postnew()
        post.post_title = post_title
        post.post_content = post_content
        post.post_owner=post_owner

        post.save()
        print("post saved")
        return redirect('profile')
    else:
        return render(req, 'login.html')

def post(req):
    template = loader.get_template('post.html')
    data = {}
    res = template.render(data, req)
    return HttpResponse(res)

