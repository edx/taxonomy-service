# Generated by Django 3.1.1 on 2020-09-09 04:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='The title of job.', max_length=255)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='JobSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(blank=True, help_text='The name of the skill required for the job.', max_length=255)),
                ('significance', models.FloatField(help_text='The significance of skill for the job.')),
                ('unique_postings', models.FloatField(help_text='The unique_postings threshold of skill for the job.')),
                ('job', models.ForeignKey(help_text='The ID of the job title extracted for the skill.', on_delete=django.db.models.deletion.CASCADE, to='taxonomy.job')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]