# Generated by Django 5.0.6 on 2024-05-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=200),
        ),
    ]
