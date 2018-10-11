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
            0:'血清',1:'血浆',2:'组织',

        }
        return  eval(arg)[value]