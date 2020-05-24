# Generated by Django 3.0.6 on 2020-05-23 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('singers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration', models.TimeField()),
                ('date_post', models.DateTimeField(auto_now_add=True)),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singers.Singers')),
            ],
        ),
    ]
