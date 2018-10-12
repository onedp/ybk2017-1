from django.shortcuts import render
from ybk.models import *
from django.db.models import Q
# Create your views here.




def fenzh(request):
    q1 = Q()
    q1.connector = 'AND'
    q2 = Q()
    q2.connector = 'AND'
    q1.children.append(('specimen_state__lt', 2))
    q1.children.append(('specimen_state', 2))

    try:
        tm=request.GET.get('timel')
        lx=request.GET.get('lx')
        q1.children.append(('classf',lx))
        q2.children.append(('classf',lx))
        q2.children.append(('fentime',tm))
        sap = Specimen.objects.filter(q1).values('num', 'name', 'classf', 'specimen_info__blh')
        fensap = Specimen.objects.filter(q2).values('num', 'name', 'classf', 'specimen_info__blh')

        return render(request, 'fenzh.html',{'sap':sap,'fensap':sap})
    except:
        pass







    return render(request,'fenzh.html')
