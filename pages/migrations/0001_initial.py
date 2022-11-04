# Generated by Django 4.1 on 2022-10-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('facebook_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('google_plus_link', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]