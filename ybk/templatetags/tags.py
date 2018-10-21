from django import template

from django.core.exceptions import FieldDoesNotExist
from django.utils.safestring import mark_safe
from django.utils.timezone import datetime,timedelta

from ybk.models import *
register = template.Library()


@register.simple_tag()
def sample_pos2specimen(value):
    print(value,"asasa")
    sam=Sample_info.objects.get(snum=value)
    sname=sam.num.specimen_info.name
    return sname


@register.filter('list')
def do_list(value):
    return range(1, value+1)

@register.filter(name='displayName')
def display_ame(value, arg):

        sex={
            1:'男',
            0:'女',
            2:'不详',

        }


        classf = {

            0:'全血', 1:'尿', 2:'精子', 3:'精浆', 5:'颗粒细胞', 4:'卵泡液', 6:'血清', 7:'血浆', 8:'白细胞',9:'血细胞',10:'胎盘',11:'脐带', 12:'毛发'
        }

        lx={0:"全血",1:"尿",2:"组织",3:"精液",4:"卵泡液",5:"毛发",}



        return  eval(arg)[value]