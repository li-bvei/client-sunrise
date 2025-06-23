from django.urls import path
from core.views_dependent import (
    list_dependents_by_basic_identity,
    detail_dependent,
    create_dependent,
    update_dependent,
    delete_dependent



)

from core.views_basic_identity import (
    list_basic_identity,
    detail_basic_identity,
    create_basic_identity,
    update_basic_identity,
    delete_basic_identity,
)
from core.thing import (
    list_api,
    detail,
    create,
    update,
    delete,
)


urlpatterns = [
    path('basic_identity/list', list_basic_identity),
    path('basic_identity/detail', detail_basic_identity),
    path('basic_identity/create', create_basic_identity),
    path('basic_identity/update', update_basic_identity),
    path('basic_identity/delete', delete_basic_identity),
    path('thing/list', list_api),
    path('thing/detail', detail),
    path('thing/create', create),
    path('thing/update', update),
    path('thing/delete', delete),
    path('dependent/list_by_basic_identity', list_dependents_by_basic_identity),
    path('dependent/detail', detail_dependent),
    path('dependent/create', create_dependent),
    path('dependent/update', update_dependent),
    path('dependent/delete', delete_dependent),
]
