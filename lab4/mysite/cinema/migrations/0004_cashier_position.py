# Generated by Django 4.2.1 on 2023-09-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_cashier_email_cashier_phone_number_cashier_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashier',
            name='position',
            field=models.CharField(default='cashier', max_length=50),
        ),
    ]