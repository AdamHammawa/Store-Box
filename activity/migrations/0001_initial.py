# Generated by Django 4.0.3 on 2023-05-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaveDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('gallery', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('document', models.ImageField(blank=True, null=True, upload_to='documents/')),
            ],
        ),
    ]
