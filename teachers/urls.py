from django.contrib import admin
from django.urls import include, path
from . import views 



urlpatterns = [
	# path('admission/',include('admission.urls')),
    path('teachers',views.teachers_list, name='teachers_url'),

]