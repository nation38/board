# Generated by Django 3.2.9 on 2021-12-02 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('site_url', models.TextField()),
                ('comment', models.TextField()),
                ('impo', models.BooleanField()),
            ],
        ),
    ]
