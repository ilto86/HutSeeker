# Generated by Django 4.2.1 on 2023-06-24 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('huts', '0005_rename_moth_month'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='approach',
            options={'verbose_name_plural': 'Approach'},
        ),
        migrations.AlterModelOptions(
            name='month',
            options={'verbose_name_plural': 'Month'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='weathercondition',
            options={'verbose_name_plural': 'Weather Condition'},
        ),
    ]
