# Generated by Django 3.2.7 on 2021-09-03 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0002_alter_pokemon_base_stats'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BaseStats',
        ),
    ]
