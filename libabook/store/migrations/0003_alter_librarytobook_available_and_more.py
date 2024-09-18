# Generated by Django 5.1.1 on 2024-09-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_book_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarytobook',
            name='available',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='librarytobook',
            name='booked',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]