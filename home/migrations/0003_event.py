# Generated by Django 4.0.4 on 2022-06-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_register_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegename', models.CharField(default='', max_length=122)),
                ('eventname', models.CharField(default='', max_length=122)),
                ('date', models.DateField()),
                ('desc', models.TextField()),
                ('image', models.ImageField(default='', upload_to='home/images')),
            ],
        ),
    ]
