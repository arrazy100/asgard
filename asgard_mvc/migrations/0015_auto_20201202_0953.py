# Generated by Django 3.1.3 on 2020-12-02 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asgard_mvc', '0014_auto_20201202_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armodel',
            name='marker_pattern_url',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='armodel',
            name='model_scale_x',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='armodel',
            name='model_scale_y',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='armodel',
            name='model_scale_z',
            field=models.IntegerField(),
        ),
    ]
