# Generated by Django 4.2.1 on 2023-05-25 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='techSkills',
            field=models.CharField(default=datetime.datetime(2023, 5, 25, 6, 21, 3, 669631, tzinfo=datetime.timezone.utc), max_length=1000),
            preserve_default=False,
        ),
    ]
