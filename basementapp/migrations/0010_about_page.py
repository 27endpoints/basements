# Generated by Django 4.2 on 2024-02-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basementapp', '0009_home_page_remove_mastermodel_base_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
