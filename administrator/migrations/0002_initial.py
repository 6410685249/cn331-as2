# Generated by Django 4.2.5 on 2023-09-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrator', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='List_students', to='users.student'),
        ),
    ]
