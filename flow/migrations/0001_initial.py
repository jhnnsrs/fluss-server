# Generated by Django 3.2 on 2021-04-13 14:37

from django.db import migrations, models
import namegenerator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlowNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arkitekt_id', models.CharField(help_text='The identifier on the Arkitekt platform', max_length=1000, unique=True)),
                ('name', models.CharField(help_text='The name of this Flow', max_length=100)),
            ],
            options={
                'arkitekt': True,
            },
        ),
        migrations.CreateModel(
            name='FlowPod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arkitekt_pod', models.CharField(help_text='The Corresponding Pod in Arnheim', max_length=1000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlowTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arkitekt_id', models.CharField(help_text='The Template this one belongs two (Arkitekt identifier)', max_length=4000, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='1.0alpha', max_length=100)),
                ('name', models.CharField(default=namegenerator.gen, max_length=100, null=True)),
                ('diagram', models.JSONField(blank=True, null=True)),
                ('description', models.CharField(blank=True, default='Add a Description', max_length=50000, null=True)),
            ],
            options={
                'arkitekt': True,
            },
        ),
    ]
