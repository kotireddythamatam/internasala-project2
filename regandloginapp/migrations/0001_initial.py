# Generated by Django 2.1.7 on 2019-05-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regmodel',
            fields=[
                ('user_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
                ('conform_password', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('mobile_number', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]