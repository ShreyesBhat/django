# Generated by Django 3.2.8 on 2021-10-26 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211025_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='roomcode',
            new_name='code',
        ),
    ]
