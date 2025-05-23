# Generated by Django 5.2.1 on 2025-05-13 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_faqcategory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqcategory',
            name='description',
            field=models.TextField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='FAQQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.faqcategory')),
            ],
        ),
        migrations.DeleteModel(
            name='FAQ',
        ),
    ]
