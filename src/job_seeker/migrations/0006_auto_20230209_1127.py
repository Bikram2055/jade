# Generated by Django 3.2.12 on 2023-02-09 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0005_auto_20230208_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_seeker',
            name='skill',
            field=models.ManyToManyField(to='job_seeker.Skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=models.CharField(max_length=50),
        ),
    ]
