from rest_framework import serializers
from messaging.models import Channel

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(max_value=None, min_value=None)
    username = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)

class ChannelSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=22)
    description = serializers.CharField(max_length=250)
    private = serializers.BooleanField()
    members = UserSerializer(many=True, read_only=True)
    createdAt = serializers.DateTimeField()
    editedAt = serializers.DateTimeField()
    creator = UserSerializer(read_only=True)

    def create(self, validated_data):
        return Channel.objects.create(**validated_data)

class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    channel_id = ChannelSerializer()
    body = serializers.CharField(max_length=500)
    createdAt = serializers.DateTimeField()
    editedAt = serializers.DateTimeField()
    creator = UserSerializer(read_only=True)