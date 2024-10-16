# Generated by Django 5.0.9 on 2024-10-13 23:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0010_usersubscription_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='subscription',
            field=models.ForeignKey(blank=True, db_column='product', null=True, on_delete=django.db.models.deletion.SET_NULL, to='subscriptions.subscription'),
        ),
    ]