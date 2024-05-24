# Generated by Django 4.2.2 on 2023-06-20 07:04

from django.db import migrations, models
from django.core.validators import RegexValidator

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Syndrome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_envoyé', models.CharField(max_length=20,validators=[RegexValidator(r'^[01]*$', 'Entrez des 0 et des 1 uniquement.')])),
                ('code_reçu', models.CharField(max_length=20,validators=[RegexValidator(r'^[01]*$', 'Entrez des 0 et des 1 uniquement.')])),
                ('valeur_syndrome', models.CharField(max_length=20,validators=[RegexValidator(r'^[01]*$', 'Entrez des 0 et des 1 uniquement.')])),
                ('état', models.CharField(max_length=20)),

            ],
        ),
    ]
