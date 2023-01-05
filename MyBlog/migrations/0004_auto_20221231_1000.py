# Generated by Django 3.2.5 on 2022-12-31 02:00

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0003_auto_20221218_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(blank=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
