# Generated by Django 4.1.7 on 2023-03-30 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_remove_achievement_certtificate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='url',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
