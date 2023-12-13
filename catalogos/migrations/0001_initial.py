# Generated by Django 4.1 on 2023-11-27 14:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('responsable', models.CharField(max_length=40, null=True)),
                ('cp', models.CharField(default=0, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=30)),
                ('apPaterno', models.CharField(max_length=30)),
                ('apMaterno', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('curp', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=60)),
                ('cp', models.CharField(max_length=5)),
                ('edad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niv', models.CharField(help_text='Indica NIV del vehiculo', max_length=20)),
                ('noMotor', models.CharField(blank=True, max_length=30)),
                ('marca', models.CharField(max_length=40)),
                ('linea', models.CharField(max_length=40)),
                ('modelo', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'VEHICULOS',
                'db_table': 'vehiculos',
            },
        ),
        migrations.CreateModel(
            name='Placa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('numTC', models.CharField(max_length=20)),
                ('fechaAlta', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaBaja', models.DateTimeField(default=django.utils.timezone.now)),
                ('estatus', models.BooleanField(default=True)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.oficina')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.propietario')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.vehiculo')),
            ],
        ),
    ]
