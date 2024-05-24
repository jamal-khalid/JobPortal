from django.contrib import admin
from .models import Job , JobSeeker , AdminUser , APILog

# Register your models here.
admin.site.register(Job)
admin.site.register(JobSeeker)
admin.site.register(AdminUser)
admin.site.register(APILog)
