# Generated by Django 3.0.6 on 2020-08-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
