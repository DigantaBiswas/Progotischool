import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone 
from django.db.models import Q
from .models import *
# Create your views here.

def result_list(request):
	results = Results.objects.all().order_by('-upload_date')
	return render(request, 'result/result_list.html' , {'results':results})

# def result_detail(request,slug):
# 	result = get_object_or_404(Result, slug=slug)
# 	return render(request, 'result_detail.html')

def download_view(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def search_view(request):
	if 'search' in request.GET:
		keyword = request.GET['search']
		print (keyword)
		results = Results.objects.filter(result_of__icontains=keyword)
		return render(request, 'result/result_list.html' , {'results':results})

	else:
		return render(request, 'result/result_list.html')
