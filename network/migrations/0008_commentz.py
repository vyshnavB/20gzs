# Generated by Django 4.1.3 on 2023-01-12 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_page_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='commentz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=255)),
                ('fr_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
