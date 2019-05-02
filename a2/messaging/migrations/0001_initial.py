# Generated by Django 2.2 on 2019-05-01 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=22)),
                ('description', models.CharField(max_length=250)),
                ('private', models.BooleanField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('editedAt', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.CharField(max_length=500)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('editedAt', models.DateTimeField(auto_now=True)),
                ('channel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messaging.Channel')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
