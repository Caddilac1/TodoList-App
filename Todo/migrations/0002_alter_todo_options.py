# Generated by Django 5.0.6 on 2024-11-09 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['completed']},
        ),
    ]
