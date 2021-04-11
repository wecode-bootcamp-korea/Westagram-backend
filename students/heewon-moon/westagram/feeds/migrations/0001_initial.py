# Generated by Django 3.1.7 on 2021-04-11 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'feeds',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.feed')),
            ],
            options={
                'db_table': 'media',
            },
        ),
        migrations.CreateModel(
            name='FeedTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.feed')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.tag')),
            ],
            options={
                'db_table': 'feed_tags',
            },
        ),
        migrations.CreateModel(
            name='FeedLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'feed_likes',
            },
        ),
        migrations.AddField(
            model_name='feed',
            name='like',
            field=models.ManyToManyField(related_name='like', through='feeds.FeedLike', to='users.User'),
        ),
        migrations.AddField(
            model_name='feed',
            name='tag',
            field=models.ManyToManyField(through='feeds.FeedTag', to='feeds.Tag'),
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.feed'),
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(related_name='comment_like', through='feeds.CommentLike', to='users.User'),
        ),
    ]
