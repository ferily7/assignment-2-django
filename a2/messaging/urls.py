from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

url(r'users', views.UserView.as_view()),
path('channels/<int:channel_id>', views.ChannelIdView.as_view()),
path('channels/<int:channel_id>/members',  views.ChannelMembersView.as_view()),
path('messages/<int:message_id>',  views.MessageView.as_view()),
url(r'channels', views.ChannelView.as_view()),

]