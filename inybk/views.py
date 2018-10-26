from django.shortcuts import render ,HttpResponse
from ybk.models import *
from django.db.models import Q
import time
import json
from django.db.models import Count,Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
            print(fenlist)
            print(fenbiao)

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
                    spa=Sample_info(classf=aa,snum=dd.num+'-'+str(bb),fenshu=bb,tap=0,volume=cc,num_id=sp,creator_id=1)
                    spl.append(spa)

            Sample_info.objects.bulk_create(spl)
        elif gn == 'qxfz':
            print('qxfz')
            yfbiao = request.POST.get('yfbiao')
            for sp in yfbiao.split(','):
                dd=Specimen.objects.get(id=sp)
                dd.fentime='2000-01-01'
                dd.specimen_state=0
                dd.save()
                Sample_info.objects.filter(num_id=sp).delete()

            # ['lx2', '0', 'shuliang', '1', 'tiji', '2']

        elif gn=='ck':
            chakan=request.POST.get('chakan')
            cklist=Sample_info.objects.filter(num__num=chakan).values('snum','classf','volume')
            result = json.dumps(list(cklist))
            return HttpResponse(result)






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
        tm=tm.strip()
        lx=request.GET.get('lx')



        q1.children.append(('classf',lx))
        q2.children.append(('classf',lx))
        q2.children.append(('fentime',tm))
        print("a哈哈哈哈",q2,'q11111',q1)

        sap = Specimen.objects.filter(q1).values('num', 'name', 'classf', 'specimen_info__blh','id')
        fensap = Specimen.objects.filter(q2).values('num', 'name', 'classf', 'specimen_info__blh','id')

        for a in sap:
            print(a)
        for a2 in fensap:
            print("fen",a2)


        return render(request, 'fenzh.html',{'sap':sap,'fensap':fensap,'lx':lx})
    except:
        pass




    return render(request,'fenzh.html')
def cunru(request):
    q1 = Q()
    q1.connector = 'AND'
    q1.children.append(('tap__lt',2))








    return render(request,'cunru.html')

def showtable(requset):
    return render(requset,'table-test.html')





def get_ram_sum_size(asset_id):
    '''
    get the size of RAM and disk in total
    :param asset_id:  asset's id
    :return:   the size of RAM in total
    '''
    all_ram_slot = models.RAM.objects.filter(asset__id=asset_id)
    all_disk_slot = models.Disk.objects.filter(asset__id=asset_id)
    ram = 0
    for slot in all_ram_slot:
        ram = ram + slot.capacity

    disk = 0
    for slot in all_disk_slot:
        disk = disk + slot.capacity
    return ram, disk


def show_asset_in_table(request):
    '''
    专门处理在服务器资产列表里面的表格信息的方法
    :param request:
    :return:
    '''
    if request.method == "GET":
        print(request.GET)
        limit = request.GET.get('limit')  # how many items per page
        offset = request.GET.get('offset')  # how many items in total in the DB
        search = request.GET.get('search')
        sort_column = request.GET.get('sort')  # which column need to sort
        order = request.GET.get('order')  # ascending or descending
        if search:  # 判断是否有搜索字写的有吻
            all_records = Sample_info.objects.filter(tap=0,snum=search).all()
        else:
            all_records = Sample_info.objects.filter(tap=0).all() # must be wirte the line code here

        if sort_column:  # 判断是否有排序需求
            sort_column = sort_column.replace('asset_', '')
            if sort_column in ['id', 'snum', 'classf', 'volume', 'fenshu']:  # 如果排序的列表在这些内容里面
                if order == 'desc':  # 如果排序是反向
                    sort_column = '-%s' % (sort_column)
                all_records = Sample_info.objects.filter(tap=0).all().order_by(sort_column)
            elif sort_column in ['name']:

                # server__ 表示asset下的外键关联的表server下面的os_release或者其他的字段进行排序
                sort_column = "num__%s" % (sort_column)
                if order == 'desc':
                    sort_column = '-%s' % (sort_column)
                all_records = Sample_info.objects.filter(tap=0).all().order_by(sort_column)

        all_records_count = all_records.count()

        if not offset:
            offset = 0
        if not limit:
            limit = 10  # 默认是每页20行的内容，与前端默认行数一致
        pageinator = Paginator(all_records, limit)  # 开始做分页

        page = int(int(offset) / int(limit) + 1)
        response_data = {'total': all_records_count, 'rows': []}  # 必须带有rows和total这2个key，total表示总页数，rows表示每行的内容

        for asset in pageinator.page(page):
            # print('aaaa',asset.num.name)
            # ram_disk = get_ram_sum_size(asset.id)  # 获取磁盘和内存的大小
            # 下面这些asset_开头的key，都是我们在前端定义好了的，前后端必须一致，前端才能接受到数据并且请求.
            response_data['rows'].append({
                "id": '<a href="/asset/asset_list/%d" target="_blank">%d</a>' % (asset.id, asset.id),
                "snum": asset.snum if asset.snum else "",
                "classf": asset.classf if asset.classf else "",
                "volume": asset.volume if asset.volume else "",
                "fenshu": asset.fenshu if asset.fenshu else "",
                "name": asset.num.name if hasattr(asset,'num') else "",
                "creattime":asset.creattime.strftime("%Y-%m-%d") if asset.creattime else ""

            })

        return HttpResponse(json.dumps(response_data))  # 需要json处理下数据格式

