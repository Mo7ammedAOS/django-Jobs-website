from django.shortcuts import render ,redirect
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .form import JobApplicationForm , JobPostForm

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    paginator =Paginator(job_list,1) #this will show one item in the page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={'jobs':page_obj}
    return render(request,'job/job_list.html',context)

def job_detail(request,slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method =='POST':
        form = JobApplicationForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()

            return redirect(reverse('jobs:job_list'))

    else:
        form = JobApplicationForm()

    context = {'details':job_detail,'form':form}
    return render(request,'job/job_detail.html',context)

def post_job(request):
    if request.method =='POST':
        form = JobPostForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()

            return redirect(reverse('jobs:job_list'))

    else:
        form = JobPostForm()

    context = {'form':form}
    return render(request,'job/post_job.html',context)


