from django.contrib import admin
from .models import Profile, Service, Project

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'hourly_rate', 'rating', 'is_verified', 'created_at')
    list_filter = ('is_verified', 'created_at')
    search_fields = ('user__username', 'skills')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('profile', 'title', 'rate_type', 'rate', 'created_at')
    list_filter = ('rate_type', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('profile', 'title', 'start_date', 'end_date', 'is_completed')
    list_filter = ('is_completed', 'start_date', 'end_date')
    search_fields = ('title', 'description')
