from django.shortcuts import render
from .models import *
# Create your views here.
def teachers_list(request):
	teachers = Teacher.objects.all().order_by('join_date')
	return render(request, 'teachers/teacher_list.html', {'teachers':teachers})
