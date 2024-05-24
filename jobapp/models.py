from django.db import models

class JobSeeker(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

class AdminUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()

    def __str__(self):
        return self.job_title
    

class APILog(models.Model):
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    request_body = models.TextField()
    response_body = models.TextField()
    status_code = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.method} {self.path}"
