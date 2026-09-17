from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.views import signup
from jobs.views import (
    JobCreateView,
    JobDeleteView,
    JobDetailView,
    JobListView,
    JobUpdateView,
    MyApplicationsListView,
    MyJobsListView,
    apply_to_job,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('jobs/create/', JobCreateView.as_view(), name='job_create'),
    path('jobs/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('jobs/<int:pk>/apply/', apply_to_job, name='apply_to_job'),
    path('my-jobs/', MyJobsListView.as_view(), name='my_jobs'),
    path(
        'my-applications/',
        MyApplicationsListView.as_view(),
        name='my_applications',
    ),

    path('accounts/signup/', signup, name='signup'),
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login',
    ),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(next_page='job_list'),
        name='logout',
    ),
]
