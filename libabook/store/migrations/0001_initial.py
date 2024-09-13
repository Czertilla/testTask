# Generated by Django 5.1.1 on 2024-09-12 17:50

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('adress', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['adress'],
            },
        ),
        migrations.CreateModel(
            name='LibraryToBook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('available', models.IntegerField()),
                ('booked', models.IntegerField(blank=True, default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.book')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.library')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(through='store.LibraryToBook', to='store.book'),
        ),
    ]
