# Generated by Django 5.0.6 on 2024-06-27 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        #migrations.AlterField(
        #    model_name='book',
        #    name='category',
        #    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category'),
        #),
    ]