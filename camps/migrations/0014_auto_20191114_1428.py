# Generated by Django 2.2.6 on 2019-11-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0013_camp_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='positions',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='camp',
            name='positions_female',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='camp',
            name='positions_male',
            field=models.IntegerField(null=True),
        ),
    ]
