# Generated by Django 2.2.8 on 2020-07-06 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extension_status', models.SmallIntegerField(default=0)),
                ('contact_name', models.CharField(max_length=255)),
                ('extension_number', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.Branch')),
            ],
        ),
    ]
