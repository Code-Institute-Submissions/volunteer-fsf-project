# Generated by Django 2.2.6 on 2019-11-14 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0023_auto_20191114_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='required_language',
            field=models.CharField(default='English', max_length=200),
        ),
    ]
