# Generated by Django 2.2.7 on 2019-11-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleMakeCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_code_name', models.CharField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]