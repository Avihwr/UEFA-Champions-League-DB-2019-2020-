# Generated by Django 3.1.1 on 2020-09-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChampionsLeague', '0019_manager_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='Market_Value',
            field=models.FloatField(null=True),
        ),
    ]
