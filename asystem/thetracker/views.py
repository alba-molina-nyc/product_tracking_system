from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Job, Memo
from .filters import JobFilter, MemoFilter
from django.contrib.auth.mixins import PermissionRequiredMixin


class HomeView(ListView):
    model = Job
    filter = JobFilter
    template_name = 'home.html'
    

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'
    fields = '__all__'


class AddJobView(PermissionRequiredMixin, CreateView):
    permission_required = 'jobs.add_jobs'
    model = Job
    template_name = 'add_job.html'
    fields = '__all__'


class AddMemoView(PermissionRequiredMixin, CreateView):
    permission_required = 'jobs.add_jobs'
    model = Memo
    template_name = 'add_memo.html'
    fields = '__all__'


class FilterByJobView(ListView):
    model = Job
    filter = JobFilter
    template_name = 'jfilter.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = JobFilter(self.request.GET, queryset=self.get_queryset())
        return context


class FilterByMemoView(ListView):
    model = Memo
    filter = MemoFilter
    template_name = 'mfilter.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MemoFilter(self.request.GET, queryset=self.get_queryset())
        return context


