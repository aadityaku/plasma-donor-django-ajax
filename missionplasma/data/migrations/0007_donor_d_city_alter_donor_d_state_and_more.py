# Generated by Django 4.0.3 on 2022-04-04 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_remove_donor_d_city_alter_donor_d_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='d_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.city'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='d_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.state'),
        ),
        migrations.AlterField(
            model_name='requester',
            name='r_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.city'),
        ),
        migrations.AlterField(
            model_name='requester',
            name='r_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.state'),
        ),
    ]
