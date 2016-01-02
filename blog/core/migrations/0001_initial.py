# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Kategori')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug', unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Silindi mi?')),
                ('category', models.ForeignKey(to='core.Category')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image', models.ImageField(upload_to=core.models.upload_to)),
                ('post', models.ForeignKey(to='core.Post', related_name='images')),
            ],
        ),
    ]
