# Generated by Django 4.2.9 on 2024-02-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=2, unique=True)),
                ('flag', models.URLField(blank=True)),
                ('population', models.PositiveIntegerField()),
                ('capital', models.CharField(max_length=100)),
            ],
        ),
    ]