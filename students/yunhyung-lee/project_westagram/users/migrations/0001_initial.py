# Generated by Django 3.1.7 on 2021-04-05 07:18

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
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('phone_num', models.IntegerField(null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]