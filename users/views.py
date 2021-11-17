from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate

# Create your views here.
def profile(request, username):
    user1 = get_object_or_404(User, username=username)
    return render(request, "users/user/register.html",
                  {"user": user1})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.GET('email')
        password = request.POST.GET('password')
        user = User.objects.create_user(username, email, password)
        messages.add_message(request, messages.SUCCESS, "You successfully register a new account: %s" % user.name)
        return redirect('index')
    else:
        return render(request, "users/user/register.html", )


def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("pw")
    user = authenticate(username=username, password=password)
    if user is not None:
        request.session['username'] = user.username
        request.seession['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS,
                             "You have logged in successfully.")
    else:
        messages.add_message(request, messages.ERROR,
                             "Invalid username or password.")
    return redirect('index')


def logout_user(request):
    del request.session['username']
    del request.session['role']
    return redirect('events:login')
