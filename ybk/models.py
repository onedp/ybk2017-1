from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Specimen(models.Model):
    num=models.CharField(verbose_name='标本编号',max_length=32)
    name=models.CharField(verbose_name='姓名',max_length=32)
    state_list = ((0, '登记'), (1, '待分装'), (2, '已分装'),)
    specimen_state=models.SmallIntegerField(choices=state_list)
    classf_list=((0,'血'),(1,'尿'),(2,'组织'),(3,'精液'),(4,'卵泡液'),(5,'毛发'),)

    classf=models.SmallIntegerField(choices=classf_list)
    specimen_info=models.ForeignKey('Specimen_info',on_delete=models.CASCADE)
    creator=models.ForeignKey('Userlist',on_delete=models.CASCADE)
    remark=models.TextField(null=True,blank=True)
    creattime=models.DateTimeField(auto_now=True)
    fentime=models.DateField(null=True,blank=True)
    def __str__(self):
        return self.num
    class Meta:
        verbose_name_plural = "标本编号"
class Specimen_info(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    blh=models.PositiveIntegerField(null=True,blank=True)
    kh=models.PositiveIntegerField(null=True,blank=True)
    fllowup=models.PositiveIntegerField()
    age=models.PositiveIntegerField(null=True,blank=True)
    sex_list =( (0,'女'),(1,'男'),(2,'不详'),)
    sex = models.SmallIntegerField(choices=sex_list)
    creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "标本信息"
class Sample_info(models.Model):
    num=models.ForeignKey('Specimen',on_delete=models.CASCADE,)
    snum=models.CharField(verbose_name='样本编号',max_length=32)
    classf_list = ((0,'全血'),(1,'尿'),(2,'精子'),(3,'精浆'),(5,'颗粒细胞'),(4,'卵泡液'),(6,'血清'),(7,'血浆'),(8,'白细胞'),(9,'血细胞'),(10,'胎盘'),(11,'脐带'),(12,'毛发'),)
    classf = models.SmallIntegerField(choices=classf_list)
    volume=models.PositiveIntegerField(null=True,blank=True)
    creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)


    creattime=models.DateField(auto_now=True)
    def __str__(self):
        return self.snum

    class Meta:
        verbose_name_plural = "样本信息"

class Sample_pos(models.Model):
    snum=models.OneToOneField('Sample_info',on_delete=models.CASCADE)
    xy=models.PositiveSmallIntegerField(null=True,blank=True)
    box_ID=models.ForeignKey('Box',on_delete=models.CASCADE)
    tap_list=((0,'入库'),(1,'待存'),(2,'出库'),(3,'入盒'),)

    tap=models.SmallIntegerField(choices=tap_list)
    def __str__(self):
        return self.snum.snum
    class Meta:
        verbose_name_plural = "样本位置"

# db_constraint=True


class Box(models.Model):
    boxnum=models.CharField(verbose_name='BOX编号',max_length=32)
    boxtype_lsit=((0,'10*10'),(1,'12*8'),(2,'6*8'),)
    boxtype=models.SmallIntegerField(choices=boxtype_lsit)

    creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)
    def __str__(self):
        return self.boxnum

    class Meta:
        verbose_name_plural = "BOX信息"
class Box_pos(models.Model):
    boxnum = models.OneToOneField('Box',on_delete=models.CASCADE)
    xy=models.PositiveSmallIntegerField(null=True,blank=True)
    sheet_ID = models.ForeignKey('Sheet',on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "BOX位置"

class Sheet(models.Model):
    shnum = models.CharField(verbose_name='SHEET编号', max_length=32)
    sheettype_lsit = ((0,'4*3'),(1,'4*5'),(2,'4*8'),)
    sheettype = models.SmallIntegerField(choices=sheettype_lsit)

    creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)

    def __str__(self):
        return self.shnum

    class Meta:
        verbose_name_plural = "SHEET信息"
class Sheet_pos(models.Model):
    shnum=models.OneToOneField('Sheet',on_delete=models.CASCADE)
    xy = models.PositiveSmallIntegerField(null=True,blank=True)
    bank_id=models.ForeignKey('Bank',on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "SHEET位置"

class Bank(models.Model):

    bnum= models.CharField(verbose_name='BANK编号', max_length=32)
    banktype_lsit = ((0,'4*4'),(1,'4*5'),(2,'3*6'),)
    banktype = models.SmallIntegerField(choices=banktype_lsit)
    bankmark_lsit = ((0,'-80'),(1,'-30'),(2,'-196'),)
    bankmark = models.SmallIntegerField(choices=bankmark_lsit)
    creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)

    def __str__(self):
        return self.bnum

    class Meta:
        verbose_name_plural = "BANK信息"

class Userlist(models.Model):
    '''账号表'''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    roles = models.ManyToManyField("Role",blank=True,null=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    '''角色表'''
    Rolename = models.CharField(max_length=32,unique=True)
    # menus = models.ManyToManyField("Menu",blank=True)

    def __str__(self):
        return self.Rolename
    class Meta:
        verbose_name_plural = "角色"



class Apply(models.Model):
    applynum=models.CharField(max_length=32)
    applyname=models.CharField(max_length=32)
    applytext=models.TextField(null=True,blank=True)

    creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)

    check=models.NullBooleanField(null=True,blank=True)
    creattime = models.DateField(auto_now=True)
    def __str__(self):
        return self.applynum
    class Meta:
        verbose_name_plural = "申请单"


class Outlist(models.Model):
    outlist=models.CharField(max_length=32)

    creattime = models.DateField(auto_now=True)
    snum=models.ManyToManyField('Sample_info')

    creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)

    def __str__(self):
        return self.outlist

    class Meta:
        verbose_name_plural = "出库单"


class Science (models.Model):
    scinum=models.CharField('科研编号',max_length=32)
    scitext=models.TextField('项目说明',null=True,blank=True)
    Applicant=models.CharField('申请人',max_length=32,null=True,blank=True)
    Project = models.IntegerField(choices=[(0, '基因组'),(1, '转录组'),(2, '蛋白组'),(3, '表观遗传组'),],default=1)
    Test_content=models.CharField('项目',max_length=32)
    Result=models.CharField('结果',max_length=32,null=True,blank=True)
    Other=models.CharField('其他',max_length=32,null=True,blank=True)
    test_order=models.CharField('检测项目',max_length=32,null=True,blank=True)
    test_order_result=models.CharField('检测项目结果',max_length=32,null=True,blank=True)
    Detection_of_gene=models.CharField('检测基因',max_length=32,null=True,blank=True)
    Detection_of_gene_result=models.CharField('检测基因结果',max_length=32,null=True,blank=True)
    remark=models.TextField('额外记录',null=True,blank=True)


    snum = models.ManyToManyField('Sample_info',verbose_name='样本编号')
    creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)


    def __str__(self):
        return self.scinum


    class Meta:
        verbose_name_plural = "科研记录"
class Clinical (models.Model):
    num=models.ManyToManyField('Specimen')
    clitext = models.TextField(null=True,blank=True)

    creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)

    def __str__(self):
        return self.num

    class Meta:
        verbose_name_plural = "医疗记录"
class Followup (models.Model):
    Fnum = models.ManyToManyField('Specimen')
    Followuptext=models.TextField(null=True,blank=True)
    creator = models.ForeignKey('Userlist',on_delete=models.CASCADE)

    def __str__(self):
        return self.Fnum

    class Meta:
        verbose_name_plural = "随访记录"









