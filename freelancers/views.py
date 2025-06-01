from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Profile, Service, Project
from django.db.models import Q
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Registration successful!')
        return response

@login_required
def dashboard(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    services = Service.objects.filter(profile=profile)
    projects = Project.objects.filter(profile=profile)
    return render(request, 'dashboard.html', {
        'profile': profile,
        'services': services,
        'projects': projects
    })

def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    services = Service.objects.filter(profile=profile)
    projects = Project.objects.filter(profile=profile)
    skills = profile.skills.split(',') if profile.skills else []
    return render(request, 'profile.html', {
        'profile': profile,
        'skills': skills,
        'services': services,
        'projects': projects
    })

def search_freelancers(request):
    query = request.GET.get('q', '')
    freelancers = Profile.objects.filter(
        Q(user__username__icontains=query) |
        Q(skills__icontains=query)
    )
    return render(request, 'search.html', {
        'freelancers': freelancers,
        'query': query
    })

@login_required
def create_service(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        service = Service(
            profile=profile,
            title=request.POST['title'],
            description=request.POST['description'],
            rate_type=request.POST['rate_type'],
            rate=request.POST['rate']
        )
        service.save()
        messages.success(request, 'Service created successfully!')
        return redirect('dashboard')
    return render(request, 'create_service.html')
