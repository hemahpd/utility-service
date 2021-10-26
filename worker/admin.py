from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from worker.models import Worker,Job


# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display=("jobid","jobtype")

class WorkerAdmin(admin.ModelAdmin):
    list_display=("jobid","wname","wphnno","gender","experience","location","specialisation")

admin.site.register(Worker,WorkerAdmin)
admin.site.register(Job,JobAdmin)
