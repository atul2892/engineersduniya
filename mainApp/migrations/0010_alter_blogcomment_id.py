# Generated by Django 5.0.1 on 2024-03-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_alter_blogcomment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
