# Generated by Django 4.2.1 on 2023-05-25 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='main.category'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Tiket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('arrival_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='main.country')),
                ('departure_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='main.country')),
            ],
        ),
    ]
