# Generated by Django 4.1.5 on 2023-05-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0005_alter_reciepes_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciepes',
            name='description',
            field=models.CharField(default='', max_length=999999),
            preserve_default=False,
        ),
    ]