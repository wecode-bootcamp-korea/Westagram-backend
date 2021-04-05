# Generated by Django 3.1.7 on 2021-04-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=45)),
                ('phone_number', models.CharField(default=None, max_length=14)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
