# Generated by Django 5.1.7 on 2025-04-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0012_alter_club_img_emblem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='img_emblem',
            field=models.ImageField(blank=True, default='clubs/images/Default_image.png', upload_to='clubs/images/'),
        ),
    ]
