# Generated by Django 2.1.1 on 2018-09-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ybk', '0003_auto_20180909_0208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='box',
            old_name='bnum',
            new_name='boxnum',
        ),
        migrations.AlterField(
            model_name='sample_pos',
            name='tap',
            field=models.SmallIntegerField(choices=[(0, '入库'), (1, '待存'), (2, '出库'), (3, '入盒')]),
        ),
    ]
