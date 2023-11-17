# Generated by Django 4.2.7 on 2023-11-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalconsultant',
            name='history_relation',
        ),
        migrations.RemoveField(
            model_name='historicalconsultant',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalconsultant',
            name='user',
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Consultant',
        ),
        migrations.DeleteModel(
            name='HistoricalConsultant',
        ),
    ]
