from django.contrib import admin
from ybk import models
# Register your models here.
class Specimen_infoAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'blh','fllowup','sex','creator')
    search_fields = ('name',)
    list_filter = ('sex','creator')
class SCIAdmin(admin.ModelAdmin):
    list_display = ('scinum','Applicant', 'Project','Test_content','Result',)
    search_fields = ('Applicant','Test_content')
    list_filter = ('Project','Applicant')
    # fields = (('scinum','Applicant'),'scitext',('Project','Test_content','Result'),('test_order','test_order_result'),('Detection_of_gene','Detection_of_gene_result'),'remark','snum','creator')
    fieldsets = (
        ("科研信息", {'fields': [('scinum','Applicant'),'scitext',('Project','Test_content','Result')]}),
        ("实验信息", {'fields': [('test_order','test_order_result'),('Detection_of_gene','Detection_of_gene_result'),'remark',]}),
        ("样本信息", {'fields': ['snum','creator']})
    )
    filter_horizontal = ('snum',)

'''
    scinum = models.CharField('科研编号', max_length=32)
    scitext = models.TextField('项目说明', null=True, blank=True)
    Applicant = models.CharField('申请人', max_length=32)
    Project = models.IntegerField(choices=[(0, '基因组'), (1, '转录组'), (2, '蛋白组'), (3, '表观遗传组'), ], default=1)
    Test_content = models.CharField('项目', max_length=32)
    Result = models.CharField('结果', max_length=32, null=True, blank=True)
    Other = models.CharField('其他', max_length=32, null=True, blank=True)
    test_order = models.CharField('检测项目', max_length=32, null=True, blank=True)
    test_order_result = models.CharField('检测项目结果', max_length=32, null=True, blank=True)
    Detection_of_gene = models.CharField('检测基因', max_length=32, null=True, blank=True)
    Detection_of_gene_result = models.CharField('检测基因结果', max_length=32, null=True, blank=True)
    remark = models.TextField('额外记录', null=True, blank=True)

    snum = models.ManyToManyField('Sample_info', verbose_name='样本编号')
    creator = models.ForeignKey('Userlist', on_delete=models.CASCADE) 
'''
# name = models.CharField(verbose_name='姓名', max_length=32)
#     blh=models.PositiveIntegerField(null=True,blank=True)
#     kh=models.PositiveIntegerField(null=True,blank=True)
#     fllowup=models.PositiveIntegerField()
#     age=models.PositiveIntegerField(null=True,blank=True)
#     sex_list =( (0,'女'),(1,'男'),(2,'不详'),)
#     sex = models.SmallIntegerField(choices=sex_list)
#     creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)

admin.site.register(models.Specimen)
admin.site.register(models.Sample_info)
admin.site.register(models.Followup)
admin.site.register(models.Bank)
admin.site.register(models.Sheet)
admin.site.register(models.Box)
admin.site.register(models.Userlist)
admin.site.register(models.Specimen_info,Specimen_infoAdmin)
admin.site.register(models.Apply)
admin.site.register(models.Box_pos)
admin.site.register(models.Clinical)
admin.site.register(models.Outlist)
admin.site.register(models.Role)
admin.site.register(models.Sample_pos)
admin.site.register(models.Sheet_pos)
admin.site.register(models.Science,SCIAdmin)

