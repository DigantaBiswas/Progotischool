import os
import random

from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone 
from noticeboard.models import Notice
from .models import Homepage_content
from teachers.models import Teacher

# Create your views here.

def home_view(request):
	notice = Notice.objects.last()
	home_content = Homepage_content.objects.last()
	teacher = Teacher.objects.all()
	teacher = random.choice(teacher)
	context = {
		'notice': notice,
		'home_content':home_content,
		'teacher':teacher,
		}


	return render(request, 'landin_page/new_landing_page.html',context)