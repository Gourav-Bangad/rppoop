# Generated by Django 4.0.4 on 2022-06-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_profile_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilenumber',
            field=models.CharField(default='', max_length=10),
        ),
    ]
