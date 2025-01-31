# Generated by Django 3.2.16 on 2025-01-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20250124_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='total_likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='total_likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['created_at'], name='blog_commen_created_4e025c_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-total_likes'], name='blog_commen_total_l_c73f53_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-pub_date'], name='blog_post_pub_dat_b2b442_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-total_likes'], name='blog_post_total_l_6b9c44_idx'),
        ),
    ]
