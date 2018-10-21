from django.shortcuts import render
from ybk.models import *
from django.db.models import Q
import time
# Create your views here.




def fenzh(request):
    if request.method == 'POST':
        gn=request.POST.get('gn')
        if gn=='fenzhuang':
            print('执行分装功能')
            fenlist= request.POST.get('fenlist')
            fenbiao= request.POST.get('fenbiao')
            flist=[]
            hao=1
            for i in fenlist.split('&'):
                a,b =i.split('=')
                if a=='lx2':
                    lx=b
                    pass
                if a=='shuliang':
                    ci=int(b)
                    pass
                if a=='tiji':
                    v=b
                    for n in range(ci):
                        flist.append([lx,hao,v])
                        hao=hao+1
            print(flist)
            print(fenbiao)
            spl=[]




            for sp in fenbiao.split(','):
                dd=Specimen.objects.get(id=sp)
                dd.fentime=time.strftime("%Y-%m-%d", time.localtime())
                dd.specimen_state=2
                dd.save()
                for spn in flist:
                    aa,bb,cc=spn
                    spa=Sample_info(classf=aa,snum=dd.num+'-'+str(bb),volume=cc,num_id=sp,creator_id=1)
                    spl.append(spa)

            Sample_info.objects.bulk_create(spl)


            # ['lx2', '0', 'shuliang', '1', 'tiji', '2']








        else:
            print('执行其他功能')



    q1 = Q()
    q1.connector = 'AND'
    q2 = Q()
    q2.connector = 'AND'
    q1.children.append(('specimen_state__lt', 2))
    q2.children.append(('specimen_state',2))

    try:
        tm=request.GET.get('timel')
        lx=request.GET.get('lx')



        q1.children.append(('classf',lx))
        q2.children.append(('classf',lx))
        q2.children.append(('fentime',tm))
        print("a哈哈哈哈")
        sap = Specimen.objects.filter(q1).values('num', 'name', 'classf', 'specimen_info__blh','id')
        fensap = Specimen.objects.filter(q2).values('num', 'name', 'classf', 'specimen_info__blh','id')

        for a in sap:
            print(a)
        for a in fensap:
            print("fen",a)


        return render(request, 'fenzh.html',{'sap':sap,'fensap':fensap,'lx':lx})
    except:
        pass







    return render(request,'fenzh.html')
