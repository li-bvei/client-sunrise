# Generated by Django 3.2.11 on 2024-05-27 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='供应商名')),
                ('contact_info', models.CharField(max_length=100, verbose_name='联系方式')),
                ('account_info', models.CharField(max_length=100, verbose_name='账户信息')),
            ],
            options={
                'db_table': 'Vendor',
            },
        ),
    ]
