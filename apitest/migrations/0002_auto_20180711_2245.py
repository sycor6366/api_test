# Generated by Django 2.0.5 on 2018-07-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apistep',
            name='apiresult',
            field=models.CharField(max_length=10000, verbose_name='预期结果'),
        ),
    ]
