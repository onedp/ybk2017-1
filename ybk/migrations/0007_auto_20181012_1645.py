# Generated by Django 2.1 on 2018-10-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ybk', '0006_specimen_specimen_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='specimen',
            name='fentime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='classf',
            field=models.SmallIntegerField(choices=[(0, '血'), (1, '尿'), (2, '组织'), (3, '精液'), (4, '卵泡液'), (5, '毛发')]),
        ),
    ]
