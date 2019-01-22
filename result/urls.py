from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('result',views.result_list, name = 'result_url'),
    path('result/download/<path:path>',views.download_view, name = 'download_result'),
    path('result/search',views.search_view, name = 'result_search_url'),

]