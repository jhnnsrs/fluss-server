# Generated by Django 3.2.16 on 2022-12-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0003_rename_args_reactivetemplate_constants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactivetemplate',
            name='implementation',
            field=models.CharField(choices=[('ZIP', 'ZIP (Zip the data)'), ('COMBINELATEST', 'COMBINELATEST (Combine values with latest value from each stream)'), ('WITHLATEST', 'WITHLATEST (Combine a leading value with the latest value)'), ('BUFFER_COMPLETE', 'BUFFER_COMPLETE (Buffer values until complete is retrieved)'), ('BUFFER_UNTIL', 'BUFFER_UNTIL (Buffer values until signal is send)'), ('CHUNK', 'CHUNK (Chunk the data)'), ('SPLIT', 'SPLIT (Split the data)'), ('OMIT', 'OMIT (Omit the data)'), ('TO_LIST', 'TO_LIST (Convert to list)'), ('FOREACH', 'FOREACH (Foreach element in list)'), ('IF', 'IF (If condition is met)'), ('AND', 'AND (AND condition)')], default='ZIP', max_length=1000, unique=True),
        ),
    ]
