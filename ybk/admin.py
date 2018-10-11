from django.contrib import admin
from ybk import models
# Register your models here.
class Specimen_infoAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'blh','fllowup','sex','creator')
    search_fields = ('name',)
    list_filter = ('sex','creator')



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
admin.site.register(models.Science)

