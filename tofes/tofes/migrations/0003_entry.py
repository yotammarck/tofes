# Generated by Django 2.2 on 2019-05-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tofes', '0002_right_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname1', models.CharField(max_length=512)),
                ('lname1', models.CharField(max_length=512)),
            ],
        ),
    ]
