# Generated by Django 3.2.6 on 2021-08-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloom', '0018_alter_company_glassdoor_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='glassdoor_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
