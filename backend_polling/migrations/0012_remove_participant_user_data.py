# Generated by Django 2.2.10 on 2022-01-16 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_polling', '0011_auto_20220117_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='user_data',
        ),
    ]