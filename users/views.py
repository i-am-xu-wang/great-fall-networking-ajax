from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate


# Create your views here.
def profile(request, username):
    user1 = get_object_or_404(User, username=username)
    return render(request, "users/user/profile.html",
                  {"user": user1})


def change_user_role(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        user_id = request.POST.get('user_id')
        user_role = request.POST.get('user_role')
        try:
            user = User.objects.get(pk=user_id)
            user.details.role = user_role
            user.details.save()
            user.save()
            return JsonResponse(
                {'success': 'success', 'user_role': user_role},
                status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'No User found with that id.'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        request.session['username'] = username
        user = User.objects.create_user(username, email, password)
        messages.add_message(request, messages.SUCCESS, "You successfully register a new account: %s" % user.username)
        return redirect('index')
    else:
        return render(request, "users/user/register.html", )


def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("pw")
    user = authenticate(username=username, password=password)
    if user is not None:
        request.session['username'] = user.username
        request.session['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS,
                             "You have logged in successfully.")
    else:
        messages.add_message(request, messages.ERROR,
                             "Invalid username or password.")
    return redirect('index')


def logout_user(request):
    del request.session['username']
    del request.session['role']
    return redirect('index')


def edit_user(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.details.gender = request.POST.get('gender')
        user.save()
        messages.add_message(request, messages.INFO, "You successfully edit user account: %s" % user.username)

        return redirect('users:profile', username)
    else:
        return render(request, "users/user/register.html", {'user': user})
