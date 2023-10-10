# Generated by Django 3.2.21 on 2023-10-10 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qfb_main', '0005_auto_20231009_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
