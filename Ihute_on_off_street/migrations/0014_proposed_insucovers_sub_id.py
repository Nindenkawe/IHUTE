# Generated by Django 4.0.1 on 2022-04-18 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ihute_on_off_street', '0013_proposed_insucovers'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposed_insucovers',
            name='sub_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Proposed_insucovers', to=settings.AUTH_USER_MODEL),
        ),
    ]