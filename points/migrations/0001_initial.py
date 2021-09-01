# Generated by Django 3.2.6 on 2021-09-01 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('week', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.player')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='week.week')),
            ],
            options={
                'unique_together': {('player', 'week')},
            },
        ),
    ]