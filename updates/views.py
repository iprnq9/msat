from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Project, Subsystem, Timeline, GeneralSubsystem
# Create your views here.


def project_list(request):
    projects = Project.objects.filter(ongoing=True).order_by('created_date')
    return render(request, 'updates/project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    subsystems = Subsystem.objects.filter(project=project)
    timelines = Timeline.objects.filter(project=project).order_by('date')
    return render(request, 'updates/project_detail.html', {'project': project, 'subsystems': subsystems, 'timelines': timelines})


def subsystem_detail(request, pk_sub):
    general_subsystem = get_object_or_404(GeneralSubsystem, pk=pk_sub)
    subsystems = Subsystem.objects.filter(general_subsystem=general_subsystem).filter(active=True)
    return render(request, 'updates/subsystem_detail.html', {'general_subsystem': general_subsystem, 'subsystems': subsystems})


# def subsytem_detail(request, pk_proj, pk_sub):
#     subsystem = get_object_or_404(Subsystem, pk=pk_sub)
#     project = get_object_or_404(Project, pk=pk_proj)
#     subsystems = Subsystem.objects.filter(name=subsystem.name)
#     return render(request, 'updates/subsystem_detail.html', {'project': project, 'subsystem': subsystem, 'subsystems': subsystems})