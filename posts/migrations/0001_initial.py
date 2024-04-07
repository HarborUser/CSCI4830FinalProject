# Generated by Django 5.0.4 on 2024-04-07 07:11

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=75, verbose_name='Course')),
            ],
        ),
        migrations.CreateModel(
            name='CoreSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=75, verbose_name='Core Subject')),
                ('test', models.CharField(max_length=100, verbose_name='test')),
                ('courses', models.ManyToManyField(blank=True, null=True, to='posts.course')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('time_of_post', models.DateTimeField(verbose_name='Time of Post')),
                ('post_description', models.CharField(max_length=500, null=True, verbose_name='Description')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc'])], verbose_name='PDF File')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Video File')),
                ('video_website_address', models.URLField(blank=True, null=True, verbose_name='Video Adress')),
                ('test', models.CharField(max_length=100, verbose_name='test')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='all_tickets',
            field=models.ManyToManyField(blank=True, null=True, to='posts.ticket'),
        ),
    ]
