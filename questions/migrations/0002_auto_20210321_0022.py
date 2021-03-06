# Generated by Django 3.1.7 on 2021-03-21 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiChoiceAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.TextField()),
            ],
            options={
                'verbose_name': 'Multi Choice Answer',
                'verbose_name_plural': 'Multi Choice Answer',
            },
        ),
        migrations.AlterModelOptions(
            name='multichoiceuser',
            options={'verbose_name': 'Multi Choice User', 'verbose_name_plural': 'Multi choice User'},
        ),
    ]
