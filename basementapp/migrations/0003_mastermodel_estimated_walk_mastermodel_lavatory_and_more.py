# Generated by Django 4.2 on 2024-01-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basementapp', '0002_mastermodel_room_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastermodel',
            name='Estimated_walk',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mastermodel',
            name='Lavatory',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='mastermodel',
            name='Room_types',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
