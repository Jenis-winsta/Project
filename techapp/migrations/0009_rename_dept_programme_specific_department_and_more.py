# Generated by Django 5.0.2 on 2024-02-14 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0008_rename_year_year_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programme_specific',
            old_name='dept',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='programme_specific_outcome',
            old_name='dept',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='semester',
            old_name='semester',
            new_name='name',
        ),
    ]