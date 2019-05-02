from django.db import models
from django.contrib.auth.models import User

# This creates the channel model
class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=22, blank=False)
    description = models.CharField(max_length=250, blank=True)
    private = models.BooleanField(null=False)
    members = models.ManyToManyField(User, related_name="members")
    createdAt = models.DateTimeField(auto_now_add=True)
    editedAt = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, 
        null=True, blank=True, on_delete=models.SET_NULL)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.added_by = request.user
        super().save_model(request, obj, form, change)

# This creates the message model
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    createdAt = models.DateTimeField(auto_now_add=True)
    editedAt = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, 
        null=True, blank=True, on_delete=models.SET_NULL)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.added_by = request.user
        super().save_model(request, obj, form, change)
