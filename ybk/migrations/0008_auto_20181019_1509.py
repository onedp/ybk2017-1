# Generated by Django 2.1.2 on 2018-10-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ybk', '0007_auto_20181012_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='science',
            name='Applicant',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='申请人'),
        ),
        migrations.AddField(
            model_name='science',
            name='Detection_of_gene',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='检测基因'),
        ),
        migrations.AddField(
            model_name='science',
            name='Detection_of_gene_result',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='检测基因结果'),
        ),
        migrations.AddField(
            model_name='science',
            name='Other',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='其他'),
        ),
        migrations.AddField(
            model_name='science',
            name='Project',
            field=models.IntegerField(choices=[(0, '基因组'), (1, '转录组'), (2, '蛋白组'), (3, '表观遗传组')], default=1),
        ),
        migrations.AddField(
            model_name='science',
            name='Result',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='结果'),
        ),
        migrations.AddField(
            model_name='science',
            name='Test_content',
            field=models.CharField(default=123, max_length=32, verbose_name='项目'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='science',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='额外记录'),
        ),
        migrations.AddField(
            model_name='science',
            name='test_order',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='检测项目'),
        ),
        migrations.AddField(
            model_name='science',
            name='test_order_result',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='检测项目结果'),
        ),
        migrations.AlterField(
            model_name='science',
            name='scinum',
            field=models.CharField(max_length=32, verbose_name='科研编号'),
        ),
        migrations.AlterField(
            model_name='science',
            name='scitext',
            field=models.TextField(blank=True, null=True, verbose_name='项目说明'),
        ),
        migrations.AlterField(
            model_name='science',
            name='snum',
            field=models.ManyToManyField(to='ybk.Sample_info', verbose_name='样本编号'),
        ),
    ]