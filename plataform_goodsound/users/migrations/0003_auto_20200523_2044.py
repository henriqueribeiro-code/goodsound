# Generated by Django 3.0.6 on 2020-05-23 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200523_2041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['name', 'email', 'date_entry_plataform'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]