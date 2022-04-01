# Generated by Django 3.2.10 on 2022-03-31 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import namegenerator


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='template',
            field=models.CharField(blank=True, help_text='The associated Template on Arkitekt', max_length=1000, null=True),
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='1.0alpha', max_length=100)),
                ('name', models.CharField(default=namegenerator.gen, max_length=100, null=True)),
                ('diagram', models.JSONField(blank=True, null=True)),
                ('description', models.CharField(blank=True, default='Add a Description', max_length=50000, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]