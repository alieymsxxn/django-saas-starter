# Generated by Django 5.0.9 on 2024-10-15 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_email_customer_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]