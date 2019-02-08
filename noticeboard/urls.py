from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$',views.notice_detail, name ='notice_detail')
 
    path('noticeboard',views.notice_list, name = 'notice_list_url'),
    path('noticeboard/<str:slug>',views.notice_detail, name='notice_detail_url'),
    path('noticeboard/download/<path:path>',views.download_view, name = 'download_url'),
]