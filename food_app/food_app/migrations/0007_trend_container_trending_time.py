# Generated by Django 4.1.5 on 2023-05-30 10:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0006_reciepes_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trend_container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.IntegerField(blank=True, default=0)),
                ('views', models.IntegerField(blank=True, default=1)),
            ],
        ),
        migrations.AddField(
            model_name='trending',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
