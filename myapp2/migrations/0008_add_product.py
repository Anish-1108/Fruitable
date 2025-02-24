# Generated by Django 5.0.4 on 2024-06-10 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0007_delete_add_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('qyt', models.IntegerField()),
                ('des', models.TextField()),
                ('pic', models.ImageField(upload_to='img')),
                ('categories_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.categories')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.user')),
            ],
        ),
    ]
