# Generated by Django 4.2.7 on 2024-05-10 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chargebacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='creation_date',
        ),
    ]
