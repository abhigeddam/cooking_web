# Generated by Django 4.1.5 on 2023-05-06 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_app', '0004_reciepes_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciepes',
            name='user_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL),
        ),
    ]
