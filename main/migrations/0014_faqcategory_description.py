# Generated by Django 5.2.1 on 2025-05-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_faq_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqcategory',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
