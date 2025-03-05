# Generated by Django 5.1.6 on 2025-03-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('prescription_medications', models.CharField(max_length=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('manufactured_date', models.DateField()),
                ('weight', models.IntegerField()),
                ('description', models.TextField()),
                ('expired_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, default=True, upload_to='media/')),
            ],
            options={
                'verbose_name': 'medication',
                'ordering': ['created_at'],
            },
        ),
    ]
