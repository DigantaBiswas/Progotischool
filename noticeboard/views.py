import os
from django.conf import settings
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone 
from django.utils.encoding import uri_to_iri

from .models import Notice
# Create your views here.
def notice_list(request):
    notices = Notice.objects.all().order_by('-upload_date')

    paginator = Paginator(notices, 12)
    page = request.GET.get('page')
    notices = paginator.get_page(page)

    return render(request, 'noticeboard/noticeboard.html',{'notices':notices})

def notice_detail(request, slug):
    slug = uri_to_iri(slug)
    notice = get_object_or_404(Notice, slug=slug)
    return render(request,'noticeboard/notice_detail.html',{'notice':notice})





def download_view(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404