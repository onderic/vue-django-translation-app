# Generated by Django 4.2.2 on 2023-06-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0004_translation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='source_language',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='source_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='translated_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]