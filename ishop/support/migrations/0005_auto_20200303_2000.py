# Generated by Django 3.0.3 on 2020-03-03 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0004_auto_20200303_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supportmessage',
            old_name='file_url',
            new_name='image',
        ),
    ]