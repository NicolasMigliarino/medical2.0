# Generated by Django 4.2.5 on 2023-09-21 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departament', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='departament',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='departament.departament', verbose_name='Departamento'),
        ),
    ]
