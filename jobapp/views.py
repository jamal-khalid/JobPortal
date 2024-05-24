from rest_framework import viewsets
from .models import JobSeeker, AdminUser, Job , APILog
from .serializers import JobSeekerSerializer, AdminUserSerializer, JobSerializer , APILogSerializer


class JobSeekerViewSet(viewsets.ModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


# Additionally I have Created this views to only see the data from APIlog Model
# that is saving data through the custom middileware that i have created 
class APILogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  APILog.objects.all()
    serializer_class = APILogSerializer  
