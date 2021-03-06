# Generated by Django 3.2.6 on 2021-08-24 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloom', '0004_auto_20210823_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=100)),
                ('interested', models.CharField(max_length=100)),
                ('glassdoor_rating', models.PositiveIntegerField()),
                ('buisness_structure', models.CharField(max_length=100)),
                ('notes', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('first_contact_through', models.CharField(max_length=100)),
                ('notes', models.TextField()),
            ],
        ),
    ]
