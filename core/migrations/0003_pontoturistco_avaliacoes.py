# Generated by Django 4.1 on 2022-08-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0002_pontoturistco_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistco',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.avaliacao'),
        ),
    ]