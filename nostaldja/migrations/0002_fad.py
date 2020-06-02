# Generated by Django 3.0.6 on 2020-05-31 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.TextField()),
                ('description', models.TextField()),
                ('decade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.Decade')),
            ],
        ),
    ]
