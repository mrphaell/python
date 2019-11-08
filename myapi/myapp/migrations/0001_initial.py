# Generated by Django 2.2.4 on 2019-11-08 00:29

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
                ('name', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
