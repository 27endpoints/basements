# Generated by Django 4.2 on 2024-01-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basementapp', '0004_rename_ress_name_mastermodel_resident_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='landlord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_room_price', models.IntegerField(blank=True)),
                ('double_room_price', models.IntegerField(blank=True)),
                ('commune_room_price', models.IntegerField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='mastermodel',
            name='Estimated_walk',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
