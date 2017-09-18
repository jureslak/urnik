# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urnik', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rezervacija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od', models.DateTimeField()),
                ('do', models.DateTimeField()),
                ('opomba', models.CharField(blank=True, max_length=192)),
                ('osebe', models.ManyToManyField(blank=True, related_name='rezervacije', to='urnik.Oseba')),
                ('ucilnice', models.ManyToManyField(related_name='rezervacije', to='urnik.Ucilnica')),
            ],
            options={
                'verbose_name_plural': 'rezervacije',
                'default_related_name': 'rezervacije',
            },
        ),
    ]