from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Job, Memo
from .filters import JobFilter, MemoFilter
from .forms import JobSelectForm, MemoForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from . import views


# def SelectJob(request):
#     job_list = Job.objects.all()

#     if request.method == 'POST':
#         form = JobSelectForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         return render(request, 'jfilter.html')
#     print(form)
#     return render(request, {'form' : form})

# # create selection page to create a muiltple job memo
# class AddMultipleMemoView(PermissionRequiredMixin, CreateView):
#     permission_required = 'jobs.add_jobs'
#     model = Memo
#     template_name = 'add_memo.html'
#     fields = '__all__'

def create_memo(request):
    form = MemoForm()
    if request.method == 'POST':
        # print('printing post', request.POST)
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
            
    context = {
        'form': form
        
    }
    return render(request, 'memo_form.html', context)



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
    def SelectJob(self, request):
        job_list = JobFilter(self.request.GET, queryset=self.get_queryset())

        if request.method == 'POST':
            form = JobSelectForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'jfilter.html')
        print(form)
        return render(request, {'form' : form})


class FilterByMemoView(ListView):
    model = Memo
    filter = MemoFilter
    template_name = 'mfilter.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MemoFilter(self.request.GET, queryset=self.get_queryset())
        return context


