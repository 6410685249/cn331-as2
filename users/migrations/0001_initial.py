# Generated by Django 4.2.5 on 2023-09-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=6)),
                ('professor', models.CharField(max_length=128)),
                ('quota', models.IntegerField(default=0)),
                ('seat', models.IntegerField()),
            ],
        ),
    ]
