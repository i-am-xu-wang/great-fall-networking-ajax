from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    # events_list views
    path('', views.events_list, name='events_list'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search', views.search_result, name='search_result'),
    path('<int:event_id>', views.event_detail, name='event_detail'),
    path('add', views.add_event, name='add_event'),
    path('feed', views.feed_page, name='feed_page'),
    path('<int:event_id>/edit', views.edit_event, name='edit_event'),
    path('event/interation', views.event_button_interaction, name='event_interaction'),
]
