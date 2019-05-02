from django.shortcuts import render
from django.contrib.auth.models import User
from messaging.models import Channel, Message
from messaging.serializers import UserSerializer, ChannelSerializer, MessageSerializer

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


#Import APIview for viewsets API interface
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserView(APIView):
    """ Comments here """
    def get(request, format=None):
        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)
        return Response(userSerializer.data)

class ChannelView(APIView):
    """ Comments here """
    def get(self, request, format=None):
        # user = request.user.username
        channels = Channel.objects.all().filter(private=False)
        channelSerializer = ChannelSerializer(channels, many=True)


        # channels = Channel.objects.filter(members=user)
        # channelSerializer = ChannelSerializer(channels, many=True)

        return Response(channelSerializer.data, headers = {
            'content-type': 'application/json'
        })

    def post(self, request):
        channelSerializer = ChannelSerializer(data=request.data)
        if channelSerializer.is_valid():
            channelSerializer.save()
            return Response(channelSerializer.data, status=status.HTTP_201_CREATED)
        return Response(channelSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChannelIdView(APIView):
    """ Comments here """
    def get(self, request, format=None, channel_id=0):
        channel_id = self.kwargs['channel_id']
        channels = Channel.objects.filter(id=channel_id)

        messages = Message.objects.filter(id=channel_id)

        channelIdSerializer = ChannelSerializer(channels, many=True)
        messageSerializer = MessageSerializer(messages, many=True)
        return Response(messageSerializer.data)
        # return Response(channelIdSerializer.data[0]["private"])


    # def post(self, request):

class ChannelMembersView(APIView):
    """ Comments here """
    # def post(self, request):


    # def delete(self, request):


class MessageView(APIView):
    """ Comments here """
    # def patch(self, request):


    # def delete(self, request):
