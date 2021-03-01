# Generated by Django 3.1.7 on 2021-03-01 04:18

from django.db import migrations, models
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_post_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(default=1, max_length=100, verbose_name='Тэг'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=smartfields.fields.ImageField(blank=True, upload_to='images'),
        ),
    ]
