# Generated by Django 4.2.6 on 2023-12-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_maquinaria_orden_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maquinaria',
            name='fecha_creacion_m',
            field=models.DateTimeField(default="1212-01-12 12:12"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trazabilidad',
            name='fecha_creacion_t',
            field=models.DateTimeField(default="1212-01-12 12:12"),
            preserve_default=False,
        ),
    ]
