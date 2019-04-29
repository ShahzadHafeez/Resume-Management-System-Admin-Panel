from django.shortcuts import render, redirect
from .models import Member
from .models import Jo

# Create your views here.

def index(request):
    Jobss = Jo.objects.all()
    context = {'Jobss': Jobss}
    return render(request, 'crud/showJobs.html', context)

def jobForm(request):
	return render(request,'crud/CreateJob.html')


def create(request):
    job = Jo(title=request.POST['jobtitle'], descriptions=request.POST['decrpition'],designation=request.POST['designation'],required_skills=request.POST['skills'],locations=request.POST['city'],min_education=request.POST['minEdu'],min_experience=request.POST['experience'],age_requirements=request.POST['minAge'],gender=request.POST['gender'],closing_date=request.POST['date'],status=request.POST['jobstatus'],salary=request.POST['salary'],additional_benefits=request.POST['benefits'],document=request.POST['fileDoc'])
    job.save()
    return redirect('/')

def edit(request, id):
    Jobs = Jo.objects.get(id=id)
    context = {'Jobs': Jobs}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    
    job = Jo.objects.get(id=id)
    job.title = request.POST['jobtitle']
   
    job.save()
    return redirect('/crud/')


def delete(request, id):
    job = Jo.objects.get(id=id)
    job.delete()
    return redirect('/crud/')