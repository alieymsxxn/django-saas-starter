# Generated by Django 5.0.9 on 2024-10-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_usersubscription_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='product_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
