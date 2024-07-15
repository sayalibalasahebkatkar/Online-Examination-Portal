# Generated by Django 5.0.6 on 2024-07-11 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('branch', models.ManyToManyField(to='exam_management.branch')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.TextField()),
                ('question_type', models.CharField(choices=[('multiple_choice_single', 'MULTIPLE_CHOICE_SINGLE'), ('multiple_choice_multiple', 'MULTIPLE_CHOICE_MULTIPLE'), ('fill_in_the_blank', 'FILL_IN_THE_BLANK')], max_length=30)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.branch')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.stream')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('option_text', models.TextField(blank=True, null=True)),
                ('is_correct', models.BooleanField(blank=True, default=False, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.question')),
            ],
        ),
        migrations.CreateModel(
            name='FillInTheBlankAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correct_answer', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.question')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.stream'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=128)),
                ('rollno', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=100)),
                ('highestdegree', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.branch')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.college')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.stream')),
            ],
        ),
        migrations.CreateModel(
            name='StudentTest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text_answer', models.TextField(blank=True, null=True)),
                ('answered_at', models.DateTimeField(auto_now_add=True)),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam_management.option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.question')),
                ('student_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.studenttest')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.admin')),
            ],
        ),
        migrations.AddField(
            model_name='studenttest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.test'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.test'),
        ),
    ]