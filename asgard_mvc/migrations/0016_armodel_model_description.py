# Generated by Django 3.1.3 on 2020-12-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asgard_mvc', '0015_auto_20201202_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='armodel',
            name='model_description',
            field=models.TextField(default='Ini adalah deskripsi'),
        ),
    ]