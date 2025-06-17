from django.contrib import admin

# Register your models here.
from myapp.models import Classification, Thing, Tag, User, Comment,Order,Honkon_base,Vendor

admin.site.register(Classification)
admin.site.register(Tag)
admin.site.register(Thing)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Honkon_base)
admin.site.register(Vendor)

