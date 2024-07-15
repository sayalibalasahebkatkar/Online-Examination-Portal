# Generated by Django 5.0.6 on 2024-07-15 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_management', '0004_alter_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='studenttest',
            name='eligible',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('roles', models.ManyToManyField(blank=True, to='exam_management.role')),
            ],
        ),
        migrations.AlterField(
            model_name='college',
            name='registered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.user'),
        ),
        migrations.AlterField(
            model_name='test',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.user'),
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
