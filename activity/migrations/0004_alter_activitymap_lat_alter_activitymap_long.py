# Generated by Django 4.1 on 2022-09-08 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activity", "0003_alter_activitymap_lat_alter_activitymap_long"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activitymap",
            name="lat",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="activitymap",
            name="long",
            field=models.FloatField(null=True),
        ),
    ]
