# Generated by Django 2.0.13 on 2019-05-05 15:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20190505_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='user',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mentor',
            name='user',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
