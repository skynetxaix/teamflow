from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.urls import reverse_lazy
from .models import Project
# Create your views here.

class ProjectsList(ListView):
    model= Project
    template_name='projects/project_list.html'
    context_object_name= 'project_list'


class CreateProject(CreateView):
    model=Project
    fields=['project_name','project_desc']
    template_name='projects/create_project.html'
    success_url= reverse_lazy('projects:ProjectList')

    def form_valid(self, form):
        form.instance.project_own = self.request.user
        return super().form_valid(form)
    

class ProjectDetail (DetailView):
    model=Project
    template_name='projects/project_detail.html'
    context_object_name='project_detail'

class UpdateProject(UpdateView):
    model=Project
    fields=['project_name','project_desc']
    template_name='projects/update_project.html'
    success_url=reverse_lazy('projects:ProjectList')

class DeleteProject(DeleteView):
    model=Project
    template_name='projects/delete_project.html'
    success_url=reverse_lazy('projects:ProjectList')