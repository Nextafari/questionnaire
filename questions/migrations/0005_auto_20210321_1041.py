# Generated by Django 3.1.7 on 2021-03-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_multichoiceuser_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multichoiceuser',
            name='uuid',
            field=models.CharField(blank=True, default=None, max_length=150),
        ),
    ]