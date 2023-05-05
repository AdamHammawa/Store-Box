# Generated by Django 4.2 on 2023-04-06 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='store/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='store/covers/')),
            ],
        ),
        migrations.CreateModel(
            name='Pelcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='store/pdfs/')),
                ('cover', models.ImageField(upload_to='store/covers/')),
            ],
        ),
    ]