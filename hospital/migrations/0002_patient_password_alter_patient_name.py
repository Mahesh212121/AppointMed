# Generated by Django 4.2.2 on 2023-07-03 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default='M', max_length=16),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
