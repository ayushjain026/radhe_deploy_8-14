# Generated by Django 4.0.2 on 2022-05-01 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RadheInd_Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pageTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='productDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=2000)),
                ('titleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productdetails', to='RadheInd_Admin.pagetitle')),
            ],
        ),
    ]
