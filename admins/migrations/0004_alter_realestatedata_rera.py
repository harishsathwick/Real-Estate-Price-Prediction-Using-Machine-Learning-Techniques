# Generated by Django 4.1.1 on 2025-02-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_alter_realestatedata_ready_to_move_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestatedata',
            name='rera',
            field=models.IntegerField(),
        ),
    ]
