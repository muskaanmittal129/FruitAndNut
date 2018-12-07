# Generated by Django 2.1.1 on 2018-12-06 15:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20181206_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='visionandmission',
            name='mission',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
        ),
        migrations.AddField(
            model_name='visionandmission',
            name='policy',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
        ),
        migrations.AlterField(
            model_name='visionandmission',
            name='vision',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]