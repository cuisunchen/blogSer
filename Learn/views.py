from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator
import json

from .serializers import TagsSerializer
from Home.serializers import ArtSerializer

from Learn.models import Tags
from Home.models import Articles

@csrf_exempt
def learnTags(request):
    ret = {'status': 200, 'data': [], 'msg': ''}
    tag_arr = Tags.objects.all()
    tag_arr = TagsSerializer(instance=tag_arr, many=True)
    ret['data'] = json.loads(json.dumps(tag_arr.data,ensure_ascii=False))
    return JsonResponse(ret,safe=False)

@csrf_exempt
def tagArticles(request):
    if request.method != 'POST':
        return
    param = json.loads(request.body)
    ret = {'status': 200,'total': 0,'data': {'total': 20,'content':[]},'msg':''}
    aticle_arr = Articles.objects.order_by('id').filter(tagId__icontains = param['tag_id'])
    pageData = Paginator(aticle_arr, int(param['page_size']))
    aticle_arrs = ArtSerializer(instance=pageData.page(int(param['page_no'])), many=True)
    totalData = json.loads(json.dumps(aticle_arrs.data, ensure_ascii=False))
    ret['data']['content'] = totalData
    ret['data']['total'] = pageData.count
    return JsonResponse(ret)



