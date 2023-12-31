# Generated by Django 4.2.2 on 2023-07-04 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_appointment_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(default=1234, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointmentdate',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointmenttime',
            field=models.TimeField(max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctoremail',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patientemail',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='prescription',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
