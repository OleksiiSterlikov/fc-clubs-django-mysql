# Generated by Django 5.1.7 on 2025-03-31 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_club_img_emblem_alter_club_since_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='img_emblem',
            field=models.ImageField(blank=True, default='Default_image.png', null=True, upload_to='static/images/'),
        ),
    ]
