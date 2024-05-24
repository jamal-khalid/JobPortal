from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobSeekerViewSet, AdminUserViewSet, JobViewSet , APILogViewSet

router = DefaultRouter()
router.register(r'jobseekers', JobSeekerViewSet)
router.register(r'adminusers', AdminUserViewSet)
router.register(r'jobs', JobViewSet)

router.register(r'apilogs' , APILogViewSet) # additionaly created to show the apilog data 

urlpatterns = [
    path('', include(router.urls)),
]
