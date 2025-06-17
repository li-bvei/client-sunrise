from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import funding
from myapp.permission.permission import isDemoAdminUser
from django.forms.models import model_to_dict
import traceback

@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        start_time = request.GET.get("startTime", None)
        end_time = request.GET.get("endTime", None)
        fundingorders = funding.objects.all()
        if keyword:
            fundingorders = fundingorders.filter(subject__contains=keyword, delete_flg=0).order_by('-id')
        else:
            fundingorders = fundingorders.filter(delete_flg=0).order_by('-id')

        if start_time:
            fundingorders = fundingorders.filter(date__gte=start_time)
        # print(f"Parsed start_time: {start_time}") 
    
    
        if end_time:
            fundingorders = fundingorders.filter(date__lte=end_time)

        orders_list = [model_to_dict(order) for order in fundingorders]
        return APIResponse(code=0, msg='查询成功', data=orders_list)


@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        order = funding.objects.get(pk=pk)
    except funding.DoesNotExist:
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
        price = float(data.get('price', 0))
        
        funding_a = funding(
            date=data.get('date'),
            subject=data.get('subject'),
            
            
            price=price,
            
        )
        funding_a.save()
        order_dict = model_to_dict(funding_a)
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
        order = funding.objects.get(pk=pk)
    except funding.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    try:
        data = request.data
        order.date = data.get('date', order.date)
        order.subject = data.get('subject', order.subject)
        
        order.price = data.get('price', order.price)
        
     
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
        funding_ids = request.GET.get('ids')
        if not funding_ids:
            return APIResponse(code=1, msg='删除失败', data='没有提供有效的 ID')

        ids_arr = funding_ids.split(',')
        funding.objects.filter(id__in=ids_arr).update(delete_flg=1)
        return APIResponse(code=0, msg='删除成功')
    except Exception as e:
        error_message = traceback.format_exc()
        print(f"Error deleting funding: {error_message}")
        return APIResponse(code=1, msg='删除失败', data=str(e))




