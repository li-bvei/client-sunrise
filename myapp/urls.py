from django.urls import path

from myapp import views
from myapp.views.admin import order,Vendor,order2,reimburse,funding,vehicle
app_name = 'myapp'
urlpatterns = [
    # api
    path('admin/overview/count', views.admin.overview.count),
    path('admin/overview/sysInfo', views.admin.overview.sysInfo),
    path('admin/thing/list', views.admin.thing.list_api),
    path('admin/thing/detail', views.admin.thing.detail),
    path('admin/thing/create', views.admin.thing.create),
    path('admin/thing/update', views.admin.thing.update),
    path('admin/thing/delete', views.admin.thing.delete),



    path('admin/comment/list', views.admin.comment.list_api),
    path('admin/comment/create', views.admin.comment.create),
    path('admin/comment/update', views.admin.comment.update),
    path('admin/comment/delete', views.admin.comment.delete),
    path('admin/classification/list', views.admin.classification.list_api),
    path('admin/classification/create', views.admin.classification.create),
    path('admin/classification/update', views.admin.classification.update),
    path('admin/classification/delete', views.admin.classification.delete),
    path('admin/tag/list', views.admin.tag.list_api),
    path('admin/tag/create', views.admin.tag.create),
    path('admin/tag/update', views.admin.tag.update),
    path('admin/tag/delete', views.admin.tag.delete),
    path('admin/record/list', views.admin.record.list_api),
    path('admin/record/create', views.admin.record.create),
    path('admin/record/update', views.admin.record.update),
    path('admin/record/delete', views.admin.record.delete),
    path('admin/banner/list', views.admin.banner.list_api),
    path('admin/banner/create', views.admin.banner.create),
    path('admin/banner/update', views.admin.banner.update),
    path('admin/banner/delete', views.admin.banner.delete),
    path('admin/ad/list', views.admin.ad.list_api),
    path('admin/ad/create', views.admin.ad.create),
    path('admin/ad/update', views.admin.ad.update),
    path('admin/ad/delete', views.admin.ad.delete),
    path('admin/notice/list', views.admin.notice.list_api),
    path('admin/notice/create', views.admin.notice.create),
    path('admin/notice/update', views.admin.notice.update),
    path('admin/notice/delete', views.admin.notice.delete),
    path('admin/loginLog/list', views.admin.loginLog.list_api),
    path('admin/loginLog/create', views.admin.loginLog.create),
    path('admin/loginLog/update', views.admin.loginLog.update),
    path('admin/loginLog/delete', views.admin.loginLog.delete),
    path('admin/opLog/list', views.admin.opLog.list_api),
    path('admin/errorLog/list', views.admin.errorLog.list_api),
    path('admin/user/list', views.admin.user.list_api),
    path('admin/user/create', views.admin.user.create),
    path('admin/user/update', views.admin.user.update),
    path('admin/user/updatePwd', views.admin.user.updatePwd),
    path('admin/user/delete', views.admin.user.delete),
    path('admin/user/info', views.admin.user.info),
    path('admin/adminLogin', views.admin.user.admin_login),
    
    path('admin/order/list', views.admin.order.list_api),
    path('admin/order/search_product', views.admin.order.search_product),
    path('admin/order/detail', views.admin.order.detail),
    path('admin/order/create', views.admin.order.create),
    path('admin/order/update', views.admin.order.update),
    path('admin/order/delete', views.admin.order.delete),

     path('admin/order2/list', views.admin.order2.list_api),
    path('admin/order2/detail', views.admin.order2.detail),
    path('admin/order2/create', views.admin.order2.create),
    path('admin/order2/update', views.admin.order2.update),
    path('admin/order2/delete', views.admin.order2.delete),

        
    path('admin/Vendor/list', views.admin.Vendor.list_api),
    path('admin/Vendor/detail', views.admin.Vendor.detail),
    path('admin/Vendor/create', views.admin.Vendor.create),
    path('admin/Vendor/update', views.admin.Vendor.update),
    path('admin/Vendor/delete', views.admin.Vendor.delete),

    path('admin/reimburse/list', views.admin.reimburse.list_api),
    path('admin/reimburse/detail', views.admin.reimburse.detail),
    path('admin/reimburse/create', views.admin.reimburse.create),
    path('admin/reimburse/update', views.admin.reimburse.update),
    path('admin/reimburse/delete', views.admin.reimburse.delete),

    path('admin/funding/list', views.admin.funding.list_api),
    path('admin/funding/detail', views.admin.funding.detail),
    path('admin/funding/create', views.admin.funding.create),
    path('admin/funding/update', views.admin.funding.update),
    path('admin/funding/delete', views.admin.funding.delete),

    path('admin/vehicle/list', views.admin.vehicle.list_api),
    path('admin/vehicle/detail', views.admin.vehicle.detail),
    path('admin/vehicle/create', views.admin.vehicle.create),
    path('admin/vehicle/update', views.admin.vehicle.update),
    path('admin/vehicle/delete', views.admin.vehicle.delete),


]
