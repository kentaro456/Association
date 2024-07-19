# Generated by Django 4.2.2 on 2024-07-19 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_reservation', '0010_reservation_created_at_reservation_statut_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='statut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_reservation.statut'),
        ),
    ]
