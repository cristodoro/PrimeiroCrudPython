# Generated by Django 2.1 on 2018-09-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetoApp', '0003_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(),
        ),
    ]
