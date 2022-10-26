# Generated by Django 4.1.2 on 2022-10-26 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_alter_notes_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Category <built-in function id>', help_text='Choose category name', max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.category'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(default='Note <built-in function id>', help_text='Choose note title', max_length=50, verbose_name='Title'),
        ),
    ]
