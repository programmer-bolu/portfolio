# Generated by Django 3.2.25 on 2024-08-26 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_adduserdata_your_previous_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adduserdata',
            name='your_previous_work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.work'),
        ),
    ]
