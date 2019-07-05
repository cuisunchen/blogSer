# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
from .serializers import ArtSerializer,NavSerializer

from Home.models import Articles,Navs

@csrf_exempt
def nav(request):
    ret = {'status': 200,'data':[], 'msg': ''}
    navs = Navs.objects.all()
    navs_arr = NavSerializer(instance=navs,many=True)
    ret['data'] = json.loads(json.dumps(navs_arr.data,ensure_ascii=False))
    return JsonResponse(ret)

@csrf_exempt
def aticles(request):
    if request.method != 'POST':
        return
    # 前端请求的参数  前端传过来的数据需要json.loads()转换   需要注意前端传参是data还是param
    param = json.loads(request.body)
    ret = {'status': 200,'total': 0,'data': {'total': 0,'content':[]},'msg':''}
    aticle_arr =  Articles.objects.all().order_by("id") # 取数据一定要排序，不然pycham会有警告

    # 请求的页面的数据
    pageData = Paginator(aticle_arr,int(param['page_size']))
    # 序列化数据
    aticle_arrs = ArtSerializer(instance=pageData.page(int(param['page_no'])),many=True)
    # 总数据
    totalData = json.loads(json.dumps(aticle_arrs.data,ensure_ascii=False))

    ret['data']['content'] = totalData
    ret['data']['total'] = pageData.count
    return JsonResponse(ret)

@csrf_exempt
def search(request):
    if request.method != 'POST':
        return

    param = json.loads(request.body)
    ret = {'status': 200,'data': {'total': 20,'content':[]},'msg':''}
    keys = ['page_no','page_size','title']
    if any(key not in param for key in keys):
        ret['status'] = '204'
        ret['msg'] = '参数错误'
        ret['data'] = {}
        print('没有传入page_no参数')
        return JsonResponse(ret)
    searchData = Articles.objects.all().order_by("id").filter(title__icontains=param['title'])
    # 请求的页面的数据
    pageData = Paginator(searchData, int(param['page_size']))
    # 序列化数据
    searchData = ArtSerializer(instance=pageData.page(int(param['page_no'])), many=True)
    # 总数据
    totalData = json.loads(json.dumps(searchData.data, ensure_ascii=False))

    ret['data']['content'] = totalData
    ret['data']['total'] = pageData.count
    return JsonResponse(ret)
