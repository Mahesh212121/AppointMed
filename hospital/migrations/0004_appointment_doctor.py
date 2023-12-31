# Generated by Django 4.2.2 on 2023-07-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_remove_patient_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=50)),
                ('patientname', models.CharField(max_length=50)),
                ('doctoremail', models.CharField(max_length=50)),
                ('patientemail', models.CharField(max_length=50)),
                ('appointmentdate', models.DateField()),
                ('appointmenttime', models.TimeField()),
                ('symptoms', models.CharField(max_length=100)),
                ('prescription', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('phonenumber', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5)),
                ('specialization', models.CharField(max_length=50)),
            ],
        ),
    ]
