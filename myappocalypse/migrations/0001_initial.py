# Generated by Django 4.0.2 on 2022-03-05 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(blank=True, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('usefulness', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('climate', models.CharField(choices=[('Dry', 'Dry'), ('Tropical', 'Tropical'), ('Continental', 'Continental'), ('Temperate', 'Temperate'), ('Polar', 'Polar')], max_length=30)),
                ('landform', models.CharField(choices=[('Mountains', 'Mountains'), ('Hills', 'Hills'), ('Plateau', 'Plateau'), ('Plain', 'Plain'), ('Ocean', 'Ocean')], max_length=30)),
                ('environment', models.CharField(choices=[('Forest', 'Forest'), ('Rocky', 'Rocky'), ('Grassland', 'Grassland'), ('Desert', 'Desert'), ('Tundra', 'Tundra'), ('Marine', 'Marine')], max_length=30)),
                ('with_child', models.BooleanField(blank=True, null=True)),
                ('with_elder', models.BooleanField(blank=True, null=True)),
                ('with_pet', models.BooleanField(blank=True, null=True)),
                ('available_infrastructure', models.BooleanField(blank=True, null=True)),
                ('available_water', models.BooleanField(blank=True, null=True)),
                ('available_food', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('weight_bag', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('weight_user', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('climate', models.CharField(choices=[('Dry', 'Dry'), ('Tropical', 'Tropical'), ('Continental', 'Continental'), ('Temperate', 'Temperate'), ('Polar', 'Polar')], max_length=30)),
                ('landform', models.CharField(choices=[('Mountains', 'Mountains'), ('Hills', 'Hills'), ('Plateau', 'Plateau'), ('Plain', 'Plain'), ('Ocean', 'Ocean')], max_length=30)),
                ('environment', models.CharField(choices=[('Forest', 'Forest'), ('Rocky', 'Rocky'), ('Grassland', 'Grassland'), ('Desert', 'Desert'), ('Tundra', 'Tundra'), ('Marine', 'Marine')], max_length=30)),
                ('with_child', models.BooleanField(blank=True, null=True)),
                ('with_elder', models.BooleanField(blank=True, null=True)),
                ('with_pet', models.BooleanField(blank=True, null=True)),
                ('available_infrastructure', models.BooleanField(blank=True, null=True)),
                ('available_water', models.BooleanField(blank=True, null=True)),
                ('available_food', models.BooleanField(blank=True, null=True)),
                ('items', models.ManyToManyField(blank=True, related_name='items', to='myappocalypse.Item')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
