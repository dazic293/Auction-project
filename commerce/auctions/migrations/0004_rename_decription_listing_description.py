# Generated by Django 3.2.18 on 2023-03-27 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_decription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='decription',
            new_name='description',
        ),
    ]
