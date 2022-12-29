# Generated by Django 4.1.4 on 2022-12-29 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_like_likemodel_rename_post_postmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='likemodel',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='postlike', to='api.usermodel'),
            preserve_default=False,
        ),
    ]