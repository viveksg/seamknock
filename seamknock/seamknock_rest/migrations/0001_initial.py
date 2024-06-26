# Generated by Django 5.0.3 on 2024-03-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lock_geofence',
            fields=[
                ('lock_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('geofence_radius', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('emailId', models.EmailField(max_length=200, primary_key=True, serialize=False)),
                ('api_key', models.CharField(max_length=200)),
                ('api_secret', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
