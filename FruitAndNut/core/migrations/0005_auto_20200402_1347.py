# Generated by Django 2.1.5 on 2020-04-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_merge_20200124_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='principal',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='principal',
            name='education',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
