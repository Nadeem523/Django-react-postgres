# Generated by Django 2.2 on 2019-04-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190428_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='767740563993354764', max_length=255, primary_key=True, serialize=False),
        ),
    ]
