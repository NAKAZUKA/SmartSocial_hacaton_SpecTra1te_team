# Generated by Django 3.2.16 on 2024-06-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AddField(
            model_name='exhibit',
            name='img',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Картинка'),
        ),
    ]