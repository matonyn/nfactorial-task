# Generated by Django 5.0.6 on 2024-05-18 16:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoty', '0005_reviews_delete_views_alter_song_id_reviews_song'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='review',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.PositiveIntegerField(default=808, primary_key=True, serialize=False),
        ),
    ]