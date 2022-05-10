# Generated by Django 3.1.7 on 2022-04-29 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampMixin',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('writer_authorized', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('timestampmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articles.timestampmixin')),
                ('numVisits', models.IntegerField(auto_created=True, null=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('tags', models.CharField(max_length=200, null=True)),
                ('author', models.ForeignKey(default='Annon', on_delete=django.db.models.deletion.CASCADE, to='articles.users')),
            ],
            bases=('articles.timestampmixin',),
        ),
    ]
