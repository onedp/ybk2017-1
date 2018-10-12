from django.shortcuts import render , HttpResponse
from ybk.models import *
# Create your vie
def index(request):

    return render(request,'index2.html')
def test1(request,id):

    if request.method=='GET':

        pxy=int(request.GET.get('pxy',0))
        print('pxy=',pxy)



        # if 'id' in request.GET:
        #     id = request.GET['id']
        #     if id is not None:
        #         sam = Sample_info.objects.get(snum=id)
        #         sname = sam.num.specimen_info.name
        #         return HttpResponse(sname)







        print(id)
        space_num = 10
        y_num = 1
        box=Box.objects.get(boxnum=id).boxtype

        if box==0:
            space_num = 100
            y_num = 10
            sd=46
        elif box==1:
            space_num = 96
            y_num = 12
            sd=38
        elif box==2:
            space_num = 48
            y_num = 8
            sd=55

        space_list={}
        for i in range(1,space_num+1):
            space_list[i]=''
        sap = Sample_pos.objects.filter(box_ID=id).all()

        z_list = []

        for z in sap:

            z_list.append(z.xy)
            space_list[z.xy]=z


        y_list=[]
        for i in range(int(space_num/y_num)):
            y_list.append((i+1)*y_num)
        return render(request,'test.html',{"title":id,'space_list':space_list,'y_list':y_list,'z_list':z_list,'sap':sap,'sd':sd,'pxy':pxy})
from django.db.models import Q

def surch(request):




        if request.method=='POST':
            tiaojian=request.POST['tiaojian']
            tiaojian=tiaojian.lstrip(',')
            print(tiaojian)
            heji=[]
            for lie in tiaojian.split('|'):
                 heji.append(lie.split(','))
            if "男"in heji[0]:
                print("nan")
                heji[0][heji[0].index("男")]=1
            if "女"in heji[0]:
                print("nan")
                heji[0][heji[0].index("女")]=0
            if "不详"in heji[0]:
                print("nan")
                heji[0][heji[0].index("不详")]=2
            zipji=zip(heji[1],heji[2],heji[0])

            print(heji)


            q1 = Q()
            q1.connector = 'AND'
            for i in zipji:
                print (i)
                q1.children.append((i[0]+i[1], i[2]))
            q1.children.append(('sample_pos__tap',0))

            jieguo=Sample_info.objects.filter(q1)
            jieguo1=jieguo.values('snum','num','classf','id','num__num','sample_pos__box_ID','sample_pos__box_ID__box_pos','num__specimen_info__blh','num__specimen_info__kh','num__specimen_info__fllowup','num__specimen_info__sex','sample_pos__xy','num__name','sample_pos__box_ID__box_pos','sample_pos__box_ID__box_pos__sheet_ID__shnum')
            jieguo2 =Sample_info.objects.filter(q1)
            for jiaa in jieguo2:
                try:
                    jia1=jiaa.sample_pos.box_ID.box_pos.sheet_ID.shnum
                    print('结果',jia1)
                except:
                    print('结果wu')
            return render(request, 'search.html',{'jieguo':jieguo1} )


        else:
            # ffff=Sample_info.objects.filter(sample_pos__tap=).all()
            # print (ffff.snum)

            return render(request,'search.html')

from django.core import serializers
import json
def ajax2(request):
        bb=request.GET.get("id")

        sam = Sample_info.objects.get(snum=bb)
        s1= sam.num.specimen_info.name
        s2 = sam.num.specimen_info.creator
        s2=str(s2)
        s3 = sam.num.specimen_info.kh
        s4 = sam.num.specimen_info.age
        s5 = sam.num.specimen_info.blh
        s6 = sam.num.specimen_info.fllowup
        s7=sam.id


        slist=[ { 'name' : s1, 'ctor' : s2, 'kh' : s3, 'age' : s4, 'blh' : s5 , 'flup' : s6 , 'bh' : bb ,'id':s7} ]

        # print (s2)
        # ss  = serializers.serialize("json", slist)



        result = json.dumps(slist)
        return HttpResponse(result)
def bank_index(request):
    if request.method=='GET':
        bank_list=Bank.objects.all()

        bb=Bank.objects.all()[0]
        bb.get_bankmark_display()




    return render(request,"bank_index.html",{'bank_list':bank_list})
def sheet(request,id):
    listsh=[]
    sheetaa={}
    bank=Bank.objects.filter(id=id)[0]
    banksh=bank.banktype
    if banksh==0:
        bsnum=16
    elif banksh==1:
        bsnum=20
    elif banksh==2:
        bsnum=18
    sheetlist=bank.sheet_pos_set.all().values('xy','id')
    for sheet in sheetlist:
        sheetaa[sheet['xy']]=sheet['id']


    for s in range(1,bsnum+1):
        listsh.append([])
        if sheetaa.get(s):
            shtp=Sheet.objects.get(id=sheetaa.get(s)).sheettype
            if shtp==0:
                sbnum=12
            elif shtp==1:
                sbnum=20
            elif shtp==2:
                sbnum=32
            boxlist=Sheet.objects.get(id=sheetaa.get(s)).box_pos_set.all().values('xy','boxnum','boxnum__boxtype','sheet_ID__shnum','boxnum__creator__bank__bnum')
            dd={}
            for box in boxlist:
                dd[box['xy']]=[box['boxnum'],box['boxnum__boxtype'],box['sheet_ID__shnum'],box['boxnum__creator__bank__bnum']]





            for b in range(1,sbnum+1):
                listsh[s-1].append([])
                if dd.get(b):
                    listsh[s-1][b-1].append([b,dd.get(b)])
















    return render(request, "sheet.html",{'listsh':listsh,'bank':bank})



def date(request):
    return render(request,'i111ndex.html')