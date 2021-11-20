from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
import datetime
# Create your views here.
from events.models import Event, Comment


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
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.WARNING,
                                 "This username has been taken.")
            return redirect('users:register')
        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.WARNING,
                                 "This email has been used.")
        return redirect('users:register')
        user = User.objects.create_user(username, email, password)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.save()
        request.session['username'] = username
        request.session['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS, "You successfully register a new account: %s" % user.username)
        return redirect('index')
    else:
        return render(request, "users/user/register.html")


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
        #  user.password = request.POST.get('password')
        user.set_password(request.POST.get('password'))
        user.details.gender = request.POST.get('gender')
        user.save()
        messages.add_message(request, messages.INFO, "You successfully edit user account: %s" % user.username)

        return redirect('users:profile', username)
    else:
        return render(request, "users/user/register.html", {'user_account': user})


def post_comment(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        text = request.POST.get('text')
        username = request.POST.get('username')
        event_id = request.POST.get('event_id')
        try:
            event = Event.objects.get(pk=event_id)
            user = User.objects.get(username=username)
            new_comment = Comment(
                content=text,
                author=user,
                event=event
            )
            new_comment.save()
            messages.add_message(request, messages.SUCCESS, "You successfully posted a new comment.")
            return JsonResponse(
                {'success': 'success', 'content': new_comment.content, 'username': new_comment.author.username,
                 'time': new_comment.time},
                status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'No User or Event found with that id.'}, status=200)

    else:
        return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)


def edit_comment(request, comment_id):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        comment = Comment.objects.get(pk=comment_id)
        comment.content = request.POST.get('text')
        comment.time = datetime.datetime.now()
        comment.save()
        event = comment.event
        messages.add_message(request, messages.INFO, "You successfully edit the comment")
        return redirect('events:events_list')
    else:
        comment = Comment.objects.get(pk=comment_id)
        event = comment.event
        comments = fetch_comment_for_an_event(event.id)
        return render(request,
                      "events/posts/item_detail.html", {'event': event, 'comments': comments, 'comment': comment})


def delete_comment(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(pk=comment_id)
        event = comment.event
        comment.delete()
        # messages.add_message(request, messages.WARNING, "You successfully delete the comment")
        # comments = fetch_comment_for_an_event(event.id)
        return redirect('events:event_detail', event.id)
    return redirect('events:events_list')


def fetch_comment_for_an_event(event_id):
    all_comments = Comment.objects.all().order_by('-time')
    comments = []
    for comment in all_comments:
        if comment.event_id == event_id:
            comments.append(comment)
    return comments
