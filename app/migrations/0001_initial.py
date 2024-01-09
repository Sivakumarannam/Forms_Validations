# Generated by Django 4.2.7 on 2024-01-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Reenterpassword', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('ReenterEmail', models.EmailField(max_length=254)),
                ('Sdateofbirth', models.DateTimeField()),
                ('Squalification_10', models.CharField(max_length=100)),
                ('Saggregrate_10', models.IntegerField()),
                ('Squalification_12', models.CharField(max_length=100)),
                ('Saggregrate_12', models.IntegerField()),
                ('Squalification_Degree', models.CharField(max_length=100)),
                ('Saggregrate_Degree', models.IntegerField()),
            ],
        ),
    ]
