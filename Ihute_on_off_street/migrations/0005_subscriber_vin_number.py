# Generated by Django 4.0.1 on 2022-03-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ihute_on_off_street', '0004_alter_subscriber_sub_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='vin_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]