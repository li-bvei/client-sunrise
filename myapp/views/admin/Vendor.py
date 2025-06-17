from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import Vendor
from myapp.permission.permission import isDemoAdminUser
from django.forms.models import model_to_dict
import traceback
from django.views.decorators.csrf import csrf_exempt
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        if keyword:
            vendors = Vendor.objects.filter(product__contains=keyword).order_by('-name')
        else:
            vendors = Vendor.objects.all().order_by('-name')

        vendor_list = [model_to_dict(vendor) for vendor in vendors]
        return APIResponse(code=0, msg='查询成功', data=vendor_list)

@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    if request.method == 'GET':
        vendor_dict = model_to_dict(vendor)
        return APIResponse(code=0, msg='查询成功', data=vendor_dict)
@csrf_exempt
@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    try:
        data = request.data
        vendor = Vendor(
            name=data.get('name'),
            contact_info=data.get('contact_info'),
            account_info=data.get('account_info'),
            
        )
        vendor.save()
        vendor_dict = model_to_dict(vendor)
        return APIResponse(code=0, msg='创建成功', data=vendor_dict)
    except Exception as e:
        # 记录详细的错误信息
        error_message = traceback.format_exc()
        print(f"Error creating Vendor: {error_message}")
        return APIResponse(code=1, msg='参数错误', data=str(e))
@csrf_exempt
@api_view(['POST'])
# @authentication_classes([AdminTokenAuthtication])
def update(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    try:
        pk = request.GET.get('id', -1)
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    try:
        data = request.data
        vendor.name = data.get('name', vendor.name)
        vendor.contact_info = data.get('contact_info', vendor.contact_info)
        vendor.account_info = data.get('account_info', vendor.account_info)
        
        vendor.save()
        vendor_dict = model_to_dict(vendor)
        return APIResponse(code=0, msg='更新成功', data=vendor_dict)
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
        Vendor.objects.filter(id__in=ids_arr).delete()
        return APIResponse(code=0, msg='删除成功')
    except Exception as e:
        return APIResponse(code=1, msg='删除失败', data=str(e))
