# Generated by Django 3.2.8 on 2021-11-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='section',
            field=models.CharField(choices=[('-1', '--Select--'), ('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D')], max_length=100),
        ),
    ]