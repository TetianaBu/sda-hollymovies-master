# Generated by Django 3.0.7 on 2020-06-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_auto_20200604_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
