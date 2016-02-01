from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy
from models import * 

class CourseList(ListView):
	model = Course

class CourseDetail(DetailView):
	model = Course

class CourseCreation(CreateView):
	model = Course
	success_url = reverse_lazy('courses:list') #aca usamos el namespace courses y el name list que nos devolvera a cursos
	fields = ['name', 'start_date', 'end_date', 'picture']

class CourseUpdate(UpdateView):
	model = Course
	success_url = reverse_lazy('courses:list')
	fields = ['name', 'start_date', 'end_date', 'picture']

class CourseDelete(DeleteView):
	model = Course
	success_url = reverse_lazy('courses:list')