# Generated by Django 5.0.2 on 2024-02-14 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0005_rename_dept_programme_specific_dep'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programme_specific',
            old_name='dep',
            new_name='dept',
        ),
    ]
