# Generated by Django 3.2 on 2022-11-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0002_auto_20221123_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]
