# Generated by Django 4.2.3 on 2023-08-20 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_loan_date_loan_loan_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='loan_type',
        ),
    ]
