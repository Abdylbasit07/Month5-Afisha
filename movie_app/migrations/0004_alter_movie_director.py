# Generated by Django 4.1.6 on 2023-02-05 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_count', to='movie_app.director'),
        ),
    ]
