from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated

from myapp.handler import APIResponse
from core.models import BasicIdentity
from core.serializers import BasicIdentitySerializer, UpdateBasicIdentitySerializer
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.permission.permission import isDemoAdminUser
from myapp import utils


@api_view(['GET'])
def list_basic_identity(request):
    keyword = request.GET.get('keyword', None)
    if keyword:
        items = BasicIdentity.objects.filter(name__icontains=keyword).order_by('-id')
    else:
        items = BasicIdentity.objects.all().order_by('-id')
    serializer = BasicIdentitySerializer(items, many=True)
    return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def detail_basic_identity(request):
    pk = request.GET.get('id', None)
    if not pk:
        return APIResponse(code=1, msg='缺少ID参数')
    try:
        item = BasicIdentity.objects.get(pk=pk)
    except BasicIdentity.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    serializer = BasicIdentitySerializer(item)
    return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create_basic_identity(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    serializer = BasicIdentitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        utils.log_error(request, serializer.errors)
        return APIResponse(code=1, msg='创建失败', data=serializer.errors)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update_basic_identity(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    pk = request.GET.get('id') or request.data.get('id')
    if not pk:
        return APIResponse(code=1, msg='缺少ID参数')

    try:
        item = BasicIdentity.objects.get(pk=pk)
    except BasicIdentity.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = UpdateBasicIdentitySerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)
    else:
        utils.log_error(request, serializer.errors)
        return APIResponse(code=1, msg='更新失败', data=serializer.errors)


@api_view(['POST'])  # 如果改用 DELETE，请改为 ['DELETE']
@authentication_classes([AdminTokenAuthtication])
def delete_basic_identity(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    ids = request.GET.get('ids', '') or request.data.get('ids', '')
    if not ids:
        return APIResponse(code=1, msg='参数错误，未提供ids')

    ids_arr = ids.split(',')
    BasicIdentity.objects.filter(id__in=ids_arr).delete()
    return APIResponse(code=0, msg='删除成功')
