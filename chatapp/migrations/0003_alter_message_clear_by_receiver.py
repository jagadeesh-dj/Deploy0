# Generated by Django 5.1.2 on 2024-10-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_message_clear_by_receiver_message_clear_by_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='clear_by_receiver',
            field=models.BooleanField(default=False),
        ),
    ]
