# Generated by Django 4.1.5 on 2023-06-09 01:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_login',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name=''),
            preserve_default=False,
        ),
    ]
