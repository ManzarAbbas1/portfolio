# Generated by Django 5.0.6 on 2024-07-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='profile_images/')),
                ('designation', models.CharField(max_length=100)),
                ('title_line', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Header',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='content',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='number',
        ),
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='proficiency',
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default='https://example.com'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='project_images/'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(upload_to='skill_images/'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
