# Generated by Django 5.0.6 on 2024-05-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoty', '0002_user_song_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.CharField(default='<django.db.models.fields.CharField>+<django.db.models.fields.CharField>', max_length=100, primary_key=True, serialize=False),
        ),
    ]