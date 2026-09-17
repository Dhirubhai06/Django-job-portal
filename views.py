from django.contrib.auth.decorators import login_required  # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # type: ignore
from django.shortcuts import get_object_or_404, redirect  # type: ignore
from django.urls import reverse, reverse_lazy  # type: ignore
from django.utils.http import url_has_allowed_host_and_scheme  # type: ignore
from django.views.decorators.http import require_POST  # type: ignore
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView  # type: ignore

from .forms import JobForm
from .models import Application, Job


class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'all_jobs'
    ordering = ['-date_posted']

    def get_queryset(self):
        return Job.objects.select_related('posted_by').order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['applied_job_ids'] = set()

        if self.request.user.is_authenticated:
            context['applied_job_ids'] = set(
                Application.objects.filter(applicant=self.request.user)
                .values_list('job_id', flat=True)
            )

        return context


class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['already_applied'] = False

        if self.request.user.is_authenticated:
            context['already_applied'] = Application.objects.filter(
                job=self.object,
                applicant=self.request.user,
            ).exists()

        return context


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'job_form.html'

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('job_detail', kwargs={'pk': self.object.pk})


class JobOwnerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        job = self.get_object()
        return job.posted_by == self.request.user


class JobUpdateView(JobOwnerRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'job_form.html'

    def get_success_url(self):
        return reverse('job_detail', kwargs={'pk': self.object.pk})


class JobDeleteView(JobOwnerRequiredMixin, DeleteView):
    model = Job
    template_name = 'job_confirm_delete.html'
    success_url = reverse_lazy('my_jobs')


class MyJobsListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'my_jobs_list.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user).order_by('-date_posted')


@login_required
@require_POST
def apply_to_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if job.posted_by == request.user:
        return redirect('job_detail', pk=job.pk)

    Application.objects.get_or_create(job=job, applicant=request.user)

    next_url = request.POST.get('next')
    if next_url and url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
    ):
        return redirect(next_url)

    return redirect('job_detail', pk=job.pk)


class MyApplicationsListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'my_applications_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return (
            Application.objects.filter(applicant=self.request.user)
            .select_related('job', 'job__posted_by')
            .order_by('-date_applied')
        )


# Backwards-compatible names for any URLconf that imports the old lowercase classes.
job_list = JobListView
job_detail = JobDetailView
