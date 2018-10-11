from django.shortcuts import render , HttpResponse
from ybk.models import *
# Create your vie
def index(request):

    return render(request,'index2.html')
def test1(request,id):

    if request.method=='GET':
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
        return render(request,'test.html',{"title":id,'space_list':space_list,'y_list':y_list,'z_list':z_list,'sap':sap,'sd':sd})


def ajax1(request):

        return render(request,'ajax1.html',)

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