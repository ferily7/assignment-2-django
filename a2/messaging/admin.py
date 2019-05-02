from django.contrib import admin
from messaging.models import Channel, Message

# Registering Channel and Message model
admin.site.register(Channel)
admin.site.register(Message)