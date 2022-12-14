# Generated by Django 4.1 on 2022-08-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoteApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('note', models.TextField(max_length=1000)),
                ('generated_by', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
