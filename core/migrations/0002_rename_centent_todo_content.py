# Generated by Django 4.2.13 on 2024-07-02 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='centent',
            new_name='content',
        ),
    ]
