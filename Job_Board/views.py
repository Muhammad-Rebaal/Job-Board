from django.shortcuts import render,get_object_or_404
from .models import JobBoard

# Create your views here.
def index(request):
    is_active = JobBoard.objects.filter(is_active=True)
    context = {
            'job_posting':is_active,
    }
    return render(request,'Job_Board/index.html',context)

def detail(request,pk):
    job_posting = get_object_or_404(JobBoard,pk=pk,is_active=True)
    context = {
            'posting':job_posting,
    }
    return render(request,'Job_Board/detail.html',context)