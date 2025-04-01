# Generated by Django 5.1.4 on 2025-04-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('course', models.CharField(max_length=100)),
                ('total_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fees_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
