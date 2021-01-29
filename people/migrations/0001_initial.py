# Generated by Django 2.2.5 on 2021-01-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('photo', models.ImageField(upload_to='person_photos')),
                ('kind', models.CharField(choices=[('actor', 'Actor'), ('director', 'Director'), ('writer', 'Writer')], max_length=15)),
            ],
            options={
                'verbose_name_plural': 'People',
                'ordering': ['created_at'],
            },
        ),
    ]
