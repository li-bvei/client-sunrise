from rest_framework.decorators import api_view, authentication_classes
from core.models import Dependent
from core.serializers import DependentSerializer, UpdateDependentSerializer
from myapp.handler import APIResponse
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.permission.permission import isDemoAdminUser
from myapp import utils


@api_view(['GET'])
def list_dependents_by_basic_identity(request):
    """
    根据 basic_identity id 查询其所有被扶养人
    接口示例: /admin/dependent/list_by_basic_identity?id=1
    """
    basic_identity_id = request.GET.get('id')
    if not basic_identity_id:
        return APIResponse(code=1, msg='缺少id参数')

    dependents = Dependent.objects.filter(basic_identity_id=basic_identity_id).order_by('id')
    serializer = DependentSerializer(dependents, many=True)
    return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def detail_dependent(request):
    """
    根据 BasicIdentity 的 ID 获取所有被扶养人列表
    """
    pk = request.GET.get('basic_identity_id')
    if not pk:
        return APIResponse(code=1, msg='缺少 basic_identity_id 参数')

    dependents = Dependent.objects.filter(basic_identity_id=pk).order_by('id')
    serializer = DependentSerializer(dependents, many=True)

    return APIResponse(code=0, msg='查询成功', data={'dependents': serializer.data})


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create_dependent(request):
    """
    创建被扶养人
    """
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    serializer = DependentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        utils.log_error(request, serializer.errors)
        return APIResponse(code=1, msg='创建失败', data=serializer.errors)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update_dependent(request):
    """
    更新被扶养人
    """
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    pk = request.GET.get('id')
    if not pk:
        return APIResponse(code=1, msg='缺少id参数')

    try:
        dependent = Dependent.objects.get(pk=pk)
    except Dependent.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = UpdateDependentSerializer(dependent, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)
    else:
        utils.log_error(request, serializer.errors)
        return APIResponse(code=1, msg='更新失败', data=serializer.errors)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete_dependent(request):
    """
    删除被扶养人，支持批量删除
    """
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    ids = request.GET.get('ids', '')
    if not ids:
        return APIResponse(code=1, msg='参数错误，未提供ids')

    ids_arr = ids.split(',')
    Dependent.objects.filter(id__in=ids_arr).delete()
    return APIResponse(code=0, msg='删除成功')
