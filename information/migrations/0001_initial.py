# Generated by Django 4.1 on 2022-09-04 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FamilyDetail",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("img", models.ImageField(upload_to="")),
                ("update_dt", models.DateTimeField(auto_now=True)),
                ("regist_dt", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
