from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Event, regular_user, admin_user


# Create your views here.
def events_list(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        button_name = request.POST.get('button_name')
        events = Event.objects.all().order_by(button_name)
    else:
        events = Event.objects.all().order_by('date')
        # events = []
    return render(request,
                  "events/posts/list.html",
                  {"events": events}
                  )


#
# def sort_events(request):
#
#     else:
#         return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)


def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request,
                  'events/posts/item_detail.html',
                  {'event': event}
                  )


def home_page(request):
    event = Event.objects.get(pk=1)
    return render(request,
                  "events/homes/home_page.html",
                  {'event': event}
                  )


def search_result(request):
    return render(request,
                  "events/homes/search_result.html"
                  )


def feed_page(request):
    return render(request,
                  "events/posts/feeds-additional_page.html",
                  )


def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        location = request.POST.get('location')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')
        new_event = Event(
            title=title,
            location=location,
            date=date,
            time=time,
            description=description,
            organizer=request.session.get('username'),

        )
        new_event.save()
        messages.add_message(request, messages.SUCCESS, "You successfully added a new event: %s" % new_event.title)
        return render(request,
                      'events/posts/item_detail.html',
                      {'event': new_event}
                      )
    else:
        return render(request, 'events/posts/add_new_event.html')


def get_edit_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request,
                  "events/posts/add_new_event.html",
                  {"event": event}
                  )


# def post_edited_event(request, event_id):
#     event = Event.objects.get(pk=event_id)
#     if request.method == 'POST':
#         event.title = request.POST.get('title')
#         event.location = request.POST.get('location')
#         event.date = request.POST.get('date')
#         event.time = request.POST.get('time')
#         event.description = request.POST.get('description')
#         event.save()
#         messages.add_message(request, messages.SUCCESS, "You successfully edit the event: %s" % event.title)
#         return render(request,
#                       'events/posts/item_detail.html',
#                       {'event': event}
#                       )
#     else:
#         return render(request,
#                       "events/posts/add_new_event.html", {"event": event})


def event_button_interaction(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        event_id = request.POST.get('event_id')
        button_name = request.POST.get('button_name')
        try:
            event = Event.objects.get(pk=event_id)
            if button_name == 'shareButton':
                event.share_number = event.share_number + 1
            else:
                event.like_number = event.like_number + 1
            event.save()
            return JsonResponse(
                {'success': 'success', 'button_name': button_name, 'like_number': event.like_number,
                 'share_number': event.share_number},
                status=200)
        except Event.DoesNotExist:
            return JsonResponse({'error': 'No Event found with that id.'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("pw")
    if username == regular_user['username'] and password == regular_user['password'] or username == admin_user[
        'username'] and password == admin_user['password']:
        request.session['username'] = username
        request.session['role'] = 'regular'
    return redirect('index')


def logout(request):
    del request.session['username']
    del request.session['role']
    return redirect('events:login')
