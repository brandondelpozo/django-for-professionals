# Generated by Django 3.1.13 on 2022-01-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20220107_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=199)),
                ('lastname', models.CharField(max_length=199)),
            ],
        ),
    ]
