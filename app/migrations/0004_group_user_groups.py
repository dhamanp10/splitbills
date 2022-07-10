# Generated by Django 4.0.5 on 2022-06-25 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('total', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='group_images/')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.group'),
            preserve_default=False,
        ),
    ]
