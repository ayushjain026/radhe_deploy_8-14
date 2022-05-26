# Generated by Django 4.0 on 2022-05-26 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RadheInd_Admin', '0008_alter_pagetitleoption_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificateImage', models.ImageField(blank='dafault.jpg', null=True, upload_to='CompanyCertificates')),
                ('certificateName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(blank='dafault.jpg', null=True, upload_to='CompanyLogo')),
                ('Company_name', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_position', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
    ]