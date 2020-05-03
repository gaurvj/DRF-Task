# Generated by Django 2.2.12 on 2020-05-03 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=30)),
                ('tz', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=60)),
                ('end_time', models.CharField(max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.UserInfo')),
            ],
        ),
    ]
