# Generated by Django 5.0 on 2023-12-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_customuser_city_alter_customuser_pincode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='profile_pic/login_img.jpg', upload_to='profile_pic/'),
        ),
    ]