# Generated by Django 4.2.5 on 2023-09-09 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_file', models.ImageField(upload_to='images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
