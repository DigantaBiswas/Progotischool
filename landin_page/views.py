import os
from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone 
from noticeboard.models import Notice
from .models import Homepage_content

# Create your views here.

def home_view(request):
    notice = Notice.objects.last()
    home_content = Homepage_content.objects.last()
   	
    context = {
    	'notice': notice,
    	'home_content':home_content,
    }

    
    return render(request, 'landin_page/landing_page.html',context)