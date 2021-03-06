# Generated by Django 4.0.3 on 2022-04-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Creaion Time')),
                ('fname', models.CharField(max_length=255, verbose_name='First Name')),
                ('lname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=255, verbose_name='Mobile Number')),
                ('home', models.CharField(blank=True, max_length=255, null=True, verbose_name='Home Number')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email Address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
