# Generated by Django 3.1.7 on 2021-03-13 14:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('environment', models.CharField(max_length=100)),
                ('component', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('data', models.JSONField()),
            ],
        ),
    ]
