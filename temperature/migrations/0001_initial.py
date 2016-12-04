# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=4)),
                ('jan', models.DecimalField(decimal_places=2, max_digits=3)),
                ('feb', models.DecimalField(decimal_places=2, max_digits=3)),
                ('mar', models.DecimalField(decimal_places=2, max_digits=3)),
                ('apr', models.DecimalField(decimal_places=2, max_digits=3)),
                ('may', models.DecimalField(decimal_places=2, max_digits=3)),
                ('jun', models.DecimalField(decimal_places=2, max_digits=3)),
                ('jul', models.DecimalField(decimal_places=2, max_digits=3)),
                ('aug', models.DecimalField(decimal_places=2, max_digits=3)),
                ('sep', models.DecimalField(decimal_places=2, max_digits=3)),
                ('octu', models.DecimalField(decimal_places=2, max_digits=3)),
                ('nov', models.DecimalField(decimal_places=2, max_digits=3)),
                ('dec', models.DecimalField(decimal_places=2, max_digits=3)),
                ('win', models.DecimalField(decimal_places=2, max_digits=3)),
                ('spr', models.DecimalField(decimal_places=2, max_digits=3)),
                ('sumr', models.DecimalField(decimal_places=2, max_digits=3)),
                ('aut', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ann', models.DecimalField(decimal_places=2, max_digits=3)),
                ('cid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='temperature.Country')),
            ],
        ),
    ]
