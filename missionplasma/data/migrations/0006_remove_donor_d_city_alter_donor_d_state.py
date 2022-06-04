# Generated by Django 4.0.3 on 2022-04-02 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_donor_d_city_alter_donor_d_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='d_city',
        ),
        migrations.AlterField(
            model_name='donor',
            name='d_state',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.state'),
        ),
    ]
