# Generated by Django 2.0 on 2017-12-27 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=64)),
                ('page_num', models.IntegerField(null=True)),
                ('author', models.ManyToManyField(to='apporm.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=63)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='pulisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apporm.Publish'),
        ),
    ]
