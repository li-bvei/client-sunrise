from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import reimburse
from myapp.permission.permission import isDemoAdminUser
from django.forms.models import model_to_dict
import traceback
from django.db.models import Q
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        start_time = request.GET.get("startTime", None)
        end_time = request.GET.get("endTime", None)
        reimburseorders = reimburse.objects.all()
        if keyword:
            reimburseorders = reimburseorders.filter(
            Q(reimburse_subject__icontains=keyword) |
            Q(reimburse_details__icontains=keyword) |
            Q(reimburse_price__icontains=keyword) |
            Q(reimburse_location__icontains=keyword)
        ).order_by('-reimburse_date')
        else:
            reimburseorders = reimburseorders.filter(delete_flg=0).order_by('-reimburse_date')
        if start_time:
            reimburseorders = reimburseorders.filter(reimburse_date__gte=start_time)
        # print(f"Parsed start_time: {start_time}") 
    
    
    if end_time:
        reimburseorders = reimburseorders.filter(reimburse_date__lte=end_time)
    orders_list = [model_to_dict(order) for order in reimburseorders]
    return APIResponse(code=0, msg='查询成功', data=orders_list)


@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('reimburse_id', -1)
        order = reimburse.objects.get(pk=pk)
    except reimburse.DoesNotExist:
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
        unit_price = float(data.get('reimburse_price', 0))
        
        reimburse_a = reimburse(
            reimburse_date=data.get('date'),
            reimburse_subject=data.get('reimburse_subject'),
            reimburse_location=data.get('reimburse_location'),
            reimburse_details=data.get('reimburse_details'),
            reimburse_price=unit_price,
            
        )
        reimburse_a.save()
        order_dict = model_to_dict(reimburse_a)
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
        pk = request.GET.get('reimburse_id', -1)
        order = reimburse.objects.get(pk=pk)
    except reimburse.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    try:
        data = request.data
        order.reimburse_date = data.get('date', order.reimburse_date)
        order.reimburse_subject = data.get('reimburse_subject', order.reimburse_subject)
        order.reimburse_location = data.get('reimburse_location', order.reimburse_location)
        order.reimburse_price = data.get('reimburse_price', order.reimburse_price)
        order.reimburse_details = data.get('reimburse_details', order.reimburse_details)
     
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
        reimburse_ids = request.GET.get('ids')
        if not reimburse_ids:
            return APIResponse(code=1, msg='删除失败', data='没有提供有效的 ID')

        ids_arr = reimburse_ids.split(',')
        reimburse.objects.filter(reimburse_id__in=ids_arr).update(delete_flg=1)
        return APIResponse(code=0, msg='删除成功')
    except Exception as e:
        error_message = traceback.format_exc()
        print(f"Error deleting reimburse: {error_message}")
        return APIResponse(code=1, msg='删除失败', data=str(e))




