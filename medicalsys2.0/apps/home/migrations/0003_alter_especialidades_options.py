# Generated by Django 4.2.5 on 2023-09-28 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_project_especialidades'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='especialidades',
            options={'ordering': ['-created'], 'verbose_name': 'especialiadad', 'verbose_name_plural': 'especialidades'},
        ),
    ]
