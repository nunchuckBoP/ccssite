from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from timetrack.models import Timesheet, TimeEntry
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.mixins import ClassNameMixin
from timetrack.forms import TimesheetForm

# Create your views here.
class TimesheetListView(LoginRequiredMixin, ClassNameMixin, ListView):
    model = Timesheet
    template_name = 'list-view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Timesheet.objects.filter(user=self.request.user)
        context["timesheet_list"] = Timesheet.objects.filter(user=self.request.user) 
        return context
    
class TimesheetCreateView(LoginRequiredMixin, ClassNameMixin, CreateView):
    model = Timesheet
    template_name = 'form-view.html'
    form_class = TimesheetForm
    success_url = reverse_lazy('sheet-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TimesheetUpdateView(LoginRequiredMixin, ClassNameMixin, UpdateView):
    model = Timesheet
    template_name = 'form-view.html'
    form_class = TimesheetForm
    success_url = reverse_lazy('sheet-list')
    
class TimesheetDeleteView(LoginRequiredMixin, ClassNameMixin, DeleteView):
    model = Timesheet
    template_name = 'confirm.html'
    success_url = reverse_lazy('sheet-list')
    
# This view shows the timesheet with all of the time entries on it
class TimeEntryListView(LoginRequiredMixin, ClassNameMixin, ListView):
    model = TimeEntry
    template_name = 'timesheet.html'
    
    def get_queryset(self):
        timesheet_id = self.kwargs.get('timesheet_id')
        queryset = TimeEntry.objects.filter(sheet=timesheet_id).order_by('date')
        print(queryset)
        return queryset