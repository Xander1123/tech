# Generated by Django 5.2.1 on 2025-05-12 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_contactmessage_responded_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Kateqoriya Adı')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Sual')),
                ('answer', models.TextField(verbose_name='Cavab')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='main.faqcategory')),
            ],
        ),
    ]
