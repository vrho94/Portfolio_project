# Generated by Django 2.0.2 on 2019-05-26 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20190526_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='slika',
            new_name='image',
        ),
    ]
