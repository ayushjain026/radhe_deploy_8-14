# Generated by Django 4.0.4 on 2022-05-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RadheInd_Admin', '0005_alter_productdetails_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetails',
            name='productImage',
        ),
        migrations.AddField(
            model_name='pagetitleoption',
            name='productImage',
            field=models.FileField(blank=True, null=True, upload_to='ProductImage'),
        ),
    ]