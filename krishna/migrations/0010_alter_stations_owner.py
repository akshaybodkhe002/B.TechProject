# Generated by Django 4.2 on 2023-12-10 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0009_slots_s_id_alter_slots_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='Owner',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
