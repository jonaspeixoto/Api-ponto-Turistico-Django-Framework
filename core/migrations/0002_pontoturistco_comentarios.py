# Generated by Django 4.1 on 2022-08-05 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_alter_cometario_data'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistco',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.cometario'),
        ),
    ]