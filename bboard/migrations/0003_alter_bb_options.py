# Generated by Django 4.0.6 on 2023-01-31 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_rubric_alter_bb_options_alter_bb_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published'], 'verbose_name': 'Оголошення1', 'verbose_name_plural': 'Оголошення2'},
        ),
    ]
