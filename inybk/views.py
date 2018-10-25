from django.shortcuts import render ,HttpResponse
from ybk.models import *
from django.db.models import Q
import time
import json
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
    pass





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
        #     all_records = models.Asset.objects.filter(id=search, asset_type=search, business_unit=search, idc=search)
        # else:
            all_records = models.Asset.objects.all()  # must be wirte the line code here

        if sort_column:  # 判断是否有排序需求
            sort_column = sort_column.replace('asset_', '')
            if sort_column in ['id', 'asset_type', 'sn', 'name', 'management_ip', 'manufactory',
                               'type']:  # 如果排序的列表在这些内容里面
                if order == 'desc':  # 如果排序是反向
                    sort_column = '-%s' % (sort_column)
                all_records = models.Asset.objects.all().order_by(sort_column)
            elif sort_column in ['salt_minion_id', 'os_release', ]:
                # server__ 表示asset下的外键关联的表server下面的os_release或者其他的字段进行排序
                sort_column = "server__%s" % (sort_column)
                if order == 'desc':
                    sort_column = '-%s' % (sort_column)
                all_records = models.Asset.objects.all().order_by(sort_column)
            elif sort_column in ['cpu_model', 'cpu_count', 'cpu_core_count']:
                sort_column = "cpu__%s" % (sort_column)
                if order == 'desc':
                    sort_column = '-%s' % (sort_column)
                all_records = models.Asset.objects.all().order_by(sort_column)
            elif sort_column in ['rams_size', ]:
                if order == 'desc':
                    sort_column = '-rams_size'
                else:
                    sort_column = 'rams_size'
                all_records = models.Asset.objects.all().annotate(rams_size=Sum('ram__capacity')).order_by(sort_column)
            elif sort_column in [
                'localdisks_size', ]:  # using variable of localdisks_size because there have a annotation below of this line
                if order == "desc":
                    sort_column = '-localdisks_size'
                else:
                    sort_column = 'localdisks_size'
                #     annotate 是注释的功能,localdisks_size前端传过来的是这个值，后端也必须这样写，Sum方法是django里面的，不是小写的sum方法，
                # 两者的区别需要注意，Sum（'disk__capacity‘）表示对disk表下面的capacity进行加法计算，返回一个总值.
                all_records = models.Asset.objects.all().annotate(localdisks_size=Sum('disk__capacity')).order_by(
                    sort_column)

            elif sort_column in ['idc', ]:
                sort_column = "idc__%s" % (sort_column)
                if order == 'desc':
                    sort_column = '-%s' % (sort_column)
                all_records = models.Asset.objects.all().order_by(sort_column)

            elif sort_column in ['trade_date', 'create_date']:
                if order == 'desc':
                    sort_column = '-%s' % sort_column
                all_records = models.Asset.objects.all().order_by(sort_column)

        all_records_count = all_records.count()

        if not offset:
            offset = 0
        if not limit:
            limit = 20  # 默认是每页20行的内容，与前端默认行数一致
        pageinator = Paginator(all_records, limit)  # 开始做分页

        page = int(int(offset) / int(limit) + 1)
        response_data = {'total': all_records_count, 'rows': []}  # 必须带有rows和total这2个key，total表示总页数，rows表示每行的内容

        for asset in pageinator.page(page):
            ram_disk = get_ram_sum_size(asset.id)  # 获取磁盘和内存的大小
            # 下面这些asset_开头的key，都是我们在前端定义好了的，前后端必须一致，前端才能接受到数据并且请求.
            response_data['rows'].append({
                "asset_id": '<a href="/asset/asset_list/%d" target="_blank">%d</a>' % (asset.id, asset.id),
                "asset_sn": asset.sn if asset.sn else "",
                "asset_business_unit": asset.business_unit if asset.business_unit else "",
                "asset_name": asset.name if asset.name else "",
                "asset_management_ip": asset.management_ip if asset.management_ip else "",
                "asset_manufactory": asset.manufactory.manufactory if hasattr(asset, 'manufactory') else "",
                "asset_type": asset.asset_type if asset.asset_type else "",
                "asset_os_release": asset.server.os_release if hasattr(asset, 'server') else "",
                "asset_salt_minion_id": asset.server.salt_minion_id if hasattr(asset, 'server') else "",
                "asset_cpu_count": asset.cpu.cpu_count if hasattr(asset, 'cpu') else "",
                "asset_cpu_core_count": asset.cpu.cpu_core_count,
                "asset_cpu_model": asset.cpu.cpu_model if hasattr(asset, 'cpu') else "",
                "asset_rams_size": ram_disk[0] if ram_disk[0] else "",
                "asset_localdisks_size": ram_disk[1] if ram_disk[1] else "",
                "asset_admin": asset.admin.username if asset.admin else "",
                "asset_idc": asset.idc if asset.idc else "",
                "asset_trade_date": asset.trade_date.strftime('%Y-%m-%d %H:%M') if asset.trade_date else "",
                "asset_create_date": asset.create_date.strftime("%Y-%m-%d %H:%M") if asset.create_date else "",
                "update_date": asset.update_date.strftime("%Y-%m-%d %H:%M") if asset.update_date else "",
            })

        return HttpResponse(json.dumps(response_data))  # 需要json处理下数据格式

