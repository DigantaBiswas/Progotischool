from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$',views.notice_detail, name ='notice_detail')
    path('',views.home_view, name = 'home_url'),

]