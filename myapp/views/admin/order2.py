from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import Honkon_base
from myapp.permission.permission import isDemoAdminUser
from django.forms.models import model_to_dict
import traceback

@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        if keyword:
            orders = Honkon_base.objects.filter(product__contains=keyword).order_by('id')
        else:
            orders = Honkon_base.objects.all().order_by('id')

        orders_list = [model_to_dict(order) for order in orders]
        return APIResponse(code=0, msg='查询成功', data=orders_list)


@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        order = Honkon_base.objects.get(pk=pk)
    except Honkon_base.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    if request.method == 'GET':
        order_dict = model_to_dict(order)
        return APIResponse(code=0, msg='查询成功', data=order_dict)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    try:
        data = request.data
        
        # 确保转换为浮点数和整数
        unit_price = float(data.get('unit_price', 0))
        
        order = Honkon_base(
            
            vendor=data.get('vendor'),
            product=data.get('product'),
            unit_price=unit_price,
            
        )
        order.save()
        order_dict = model_to_dict(order)
        return APIResponse(code=0, msg='创建成功', data=order_dict)
    except Exception as e:
        # 记录详细的错误信息
        error_message = traceback.format_exc()
        print(f"Error creating order: {error_message}")
        return APIResponse(code=1, msg='参数错误', data=str(e))


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    try:
        pk = request.GET.get('id', -1)
        order = Honkon_base.objects.get(pk=pk)
    except Honkon_base.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    try:
        data = request.data
        
        order.vendor = data.get('vendor', order.vendor)
        order.product = data.get('product', order.product)
        order.unit_price = data.get('unit_price', order.unit_price)
     
        order.save()
        order_dict = model_to_dict(order)
        return APIResponse(code=0, msg='更新成功', data=order_dict)
    except Exception as e:
        return APIResponse(code=1, msg='参数错误', data=str(e))


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Honkon_base.objects.filter(id__in=ids_arr).delete()
        return APIResponse(code=0, msg='删除成功')
    except Exception as e:
        return APIResponse(code=1, msg='删除失败', data=str(e))
