# Generated by Django 3.0.3 on 2020-03-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=10000)),
                ('genre', models.CharField(max_length=256)),
                ('publishing_info', models.CharField(max_length=256)),
                ('cover', models.ImageField(null=True, upload_to='media')),
            ],
            options={
                'verbose_name_plural': 'Books',
            },
        ),
    ]
