# Generated by Django 2.0.7 on 2018-07-16 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geocontext', '0013_auto_20180715_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contextcache',
            name='value',
            field=models.CharField(blank=True, help_text='The value of the context.', max_length=200, null=True),
        ),
    ]