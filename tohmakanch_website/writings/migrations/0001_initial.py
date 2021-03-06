# Generated by Django 3.1.5 on 2021-01-04 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'writing',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('writing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='writings.writing')),
            ],
            options={
                'db_table': 'article',
            },
            bases=('writings.writing',),
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('writing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='writings.writing')),
            ],
            options={
                'db_table': 'poem',
            },
            bases=('writings.writing',),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('writing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='writings.writing')),
            ],
            options={
                'db_table': 'story',
            },
            bases=('writings.writing',),
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writings.writing')),
            ],
            options={
                'db_table': 'favourite',
            },
        ),
    ]
