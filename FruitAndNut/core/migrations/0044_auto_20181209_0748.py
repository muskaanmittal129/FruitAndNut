# Generated by Django 2.1.1 on 2018-12-09 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_auto_20181209_0741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='affiliation',
            old_name='affiliation_pdf',
            new_name='affiliation_image',
        ),
    ]
