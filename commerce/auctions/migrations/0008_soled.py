# Generated by Django 3.2.18 on 2023-04-04 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20230328_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('buyer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='auctions.listing')),
                ('seller', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
                ('soled_price', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid')),
            ],
        ),
    ]
