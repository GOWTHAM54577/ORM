# Generated by Django 5.0.3 on 2024-03-21 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books_DB',
            fields=[
                ('serial', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
    ]