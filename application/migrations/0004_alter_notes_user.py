# Generated by Django 4.1.2 on 2022-10-26 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
