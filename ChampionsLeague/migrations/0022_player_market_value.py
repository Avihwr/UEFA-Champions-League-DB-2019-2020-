# Generated by Django 3.1.1 on 2020-09-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChampionsLeague', '0021_auto_20200921_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='Market_Value',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
