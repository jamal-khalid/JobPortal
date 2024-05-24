import json
from .models import APILog
from django.utils.deprecation import MiddlewareMixin

class APILogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._body = request.body

    def process_response(self, request, response):
        if request.path.startswith('/api/'):
            APILog.objects.create(
                path=request.path,
                method=request.method,
                request_body=request._body.decode('utf-8'),
                response_body=response.content.decode('utf-8'),
                status_code=response.status_code,
            )
        return response