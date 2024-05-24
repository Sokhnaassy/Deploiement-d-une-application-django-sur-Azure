# Generated by Django 4.2.4 on 2023-08-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_syndrome_fonction_goppa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='pubkey',
        ),
        migrations.RemoveField(
            model_name='syndrome',
            name='fonction_goppa',
        ),
        migrations.AddField(
            model_name='syndrome',
            name='fgoppa',
            field=models.CharField(default=0, editable=False, max_length=20),
            preserve_default=False,
        ),
    ]
