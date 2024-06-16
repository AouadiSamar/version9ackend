# Generated by Django 5.0.6 on 2024-06-16 10:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rembourssement', '0003_alter_rembourssement_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rembourssement',
            options={'verbose_name': 'Rembourssement', 'verbose_name_plural': 'Rembourssement'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='rembourssement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentss', to='rembourssement.rembourssement'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentss', to=settings.AUTH_USER_MODEL),
        ),
    ]