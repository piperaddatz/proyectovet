# Generated by Django 3.1.4 on 2021-03-22 00:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0002_auto_20210321_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='profile_pic',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
