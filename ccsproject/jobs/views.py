from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from jobs.models import Job
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from jobs.forms import JobForm
from jobs.mixins import ClassNameMixin

# Create your views here.
class JobListView(LoginRequiredMixin, ClassNameMixin, ListView):
    model = Job
    template_name = 'list-view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    

class JobCreateView(LoginRequiredMixin, ClassNameMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'form-view.html'
    success_url = reverse_lazy('job-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class JobDetailView(LoginRequiredMixin, ClassNameMixin, DetailView):
    model = Job
    template_name = 'detail-view'

class JobUpdateView(LoginRequiredMixin, ClassNameMixin, UpdateView):
    model = Job
    template_name = 'form-view.html'
    form_class = JobForm
    success_url = reverse_lazy('job-list')

class JobDeleteView(LoginRequiredMixin, ClassNameMixin, DeleteView):
    model = Job
    template_name = 'confirm.html'
    success_url = reverse_lazy('job-list')