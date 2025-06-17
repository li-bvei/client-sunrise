from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import Order,Honkon_base
from myapp.permission.permission import isDemoAdminUser
from django.forms.models import model_to_dict
import traceback
from django.utils.dateparse import parse_datetime
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def list_api(request):
    keyword = request.GET.get("keyword", None)
    start_time = request.GET.get("startTime", None)
    end_time = request.GET.get("endTime", None)

    orders = Order.objects.all()

    if keyword:
        orders = orders.filter(product__icontains=keyword)
    
   
    if start_time:
        orders = orders.filter(date__gte=start_time)
        # print(f"Parsed start_time: {start_time}") 
    
    
    if end_time:
        orders = orders.filter(date__lte=end_time)

    orders_list = [model_to_dict(order) for order in orders]
    return APIResponse(code=0, msg='查询成功', data=orders_list)


@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
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
        quantity = int(data.get('quantity', 0))
        total = unit_price * quantity
        order = Order(
            date=data.get('date'),
            vendor=data.get('vendor'),
            product=data.get('product'),
            remarks = data.get('remarks'),
            unit_price=unit_price,
            quantity=quantity,
            total=total
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
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    try:
        data = request.data
        order.date = data.get('date', order.date)
        order.vendor = data.get('vendor', order.vendor)
        order.product = data.get('product', order.product)
        order.unit_price = data.get('unit_price', order.unit_price)
        order.quantity = data.get('quantity', order.quantity)
        order.total = order.price * order.quantity
        order.save()
        order_dict = model_to_dict(order)
        return APIResponse(code=0, msg='更新成功', data=order_dict)
    except Exception as e:
        print(str(e))
        return APIResponse(code=1, msg='参数错误', data=str(e))


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Order.objects.filter(id__in=ids_arr).delete()
        return APIResponse(code=0, msg='删除成功')
    except Exception as e:
        return APIResponse(code=1, msg='删除失败', data=str(e))

@api_view(['GET'])
def search_product(request):
    keyword = request.GET.get("keyword", None)
    vendor = request.GET.get("vendor", None)
    
    products = Honkon_base.objects.all()
    if vendor:
        products = products.filter(vendor__icontains=vendor)
    if keyword:
        products = products.filter(product__icontains=keyword)
    
   
    
    products_list = [model_to_dict(product) for product in products]
    
    return APIResponse(code=0, msg='查询成功', data=products_list)