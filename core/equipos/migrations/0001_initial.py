# Generated by Django 3.1.1 on 2020-11-17 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('service_tag', models.CharField(blank=True, max_length=12)),
                ('estado', models.CharField(choices=[('Pr', 'En preparacion'), ('Et', 'Entregado'), ('Ep', 'Equipo pool'), ('Pd', 'Para donación'), ('Bs', 'Basura electronica'), ('Pa', 'Pool asignado'), ('Ua', 'Usuario asignado')], default='Pr', max_length=2)),
                ('fecha_termino_garantia', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'equipo',
                'verbose_name_plural': 'equipos',
                'db_table': 'Equipos',
            },
        ),
        migrations.CreateModel(
            name='Equipo_Para_Entregar',
            fields=[
                ('id_equipo_para_entregar', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_equipo', models.CharField(max_length=12)),
                ('usuario_final', models.CharField(blank=True, max_length=20)),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.equipo')),
            ],
            options={
                'verbose_name': 'Equipo para entregar',
                'verbose_name_plural': 'Equipos para entregar',
                'db_table': 'EquipoParaEntregar',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('categoria', models.CharField(choices=[('LT', 'Laptop'), ('PC', 'Desktop')], max_length=2)),
                ('id_stock', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.SmallIntegerField()),
                ('modelo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=15)),
                ('ram', models.SmallIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stock',
                'db_table': 'Stock',
            },
        ),
        migrations.CreateModel(
            name='Equipo_Pool_Entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_salida', models.DateTimeField()),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('caso_especial', models.BooleanField(default=False)),
                ('equipo_recibido', models.BooleanField(default=False)),
                ('nombre_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.equipo_para_entregar')),
            ],
            options={
                'verbose_name': 'Equipo pool entrega',
                'verbose_name_plural': 'Equipos Pool entrega',
                'db_table': 'EquiposPoolEntrega',
            },
        ),
        migrations.CreateModel(
            name='Equipo_Para_Entregar_Detalles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configurado_por', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_preparacion', models.DateField()),
                ('check_list', models.FileField(blank=True, default='', null=True, upload_to='checkList')),
                ('certificado_de_calidad', models.FileField(blank=True, default='', null=True, upload_to='certificado')),
                ('solicitud', models.FileField(blank=True, default='', null=True, upload_to='solicitudes')),
                ('site', models.CharField(blank=True, max_length=5, null=True)),
                ('departamento', models.CharField(blank=True, max_length=30, null=True)),
                ('area', models.CharField(blank=True, max_length=30, null=True)),
                ('ubicacion_exacta', models.CharField(blank=True, max_length=30, null=True)),
                ('apps_especiales', models.CharField(blank=True, max_length=200, null=True)),
                ('registro_en_inventario', models.BooleanField(default=False)),
                ('id_equipo_para_entregar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.equipo_para_entregar')),
                ('preparado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle de entrega',
                'verbose_name_plural': 'Detalles de entrega',
                'db_table': 'DetallesEntrega',
            },
        ),
        migrations.AddField(
            model_name='equipo',
            name='id_stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.stock'),
        ),
        migrations.CreateModel(
            name='Basura_Electronica',
            fields=[
                ('id_basura_electronica', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.SmallIntegerField()),
                ('modelo', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=15)),
                ('no_serie', models.CharField(blank=True, default='N/A', max_length=100, null=True)),
                ('planta', models.CharField(choices=[('VIG', 'Villagran'), ('CEL', 'Celaya')], max_length=3)),
                ('fecha_registro', models.DateField()),
                ('recolectado', models.BooleanField()),
                ('fecha_recoleccion', models.DateField(blank=True, null=True)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Basura Electronica',
                'verbose_name_plural': 'Basura Electronica',
                'db_table': 'BasuraElectronica',
            },
        ),
    ]
