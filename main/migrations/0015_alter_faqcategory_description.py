# Generated by Django 5.2.1 on 2025-05-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_faqcategory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
