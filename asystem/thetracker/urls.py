from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('memowriter/<str:pk_test>/', views.memowriter, name="memowriter"),

    path('job_filter', FilterByJobView.as_view(), name='job-filter'),
    path('memo_filter', FilterByMemoView.as_view(), name='memo-filter'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('add_job/', AddJobView.as_view(), name='add-job'),
    path('job/<int:pk>/add_memo/', AddMemoView.as_view(), name='add-memo'),
    path('create_memo/', views.create_memo, name='create_memo'),

   
  

]