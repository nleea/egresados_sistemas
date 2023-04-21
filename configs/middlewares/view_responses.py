from django.http import HttpResponse
from ..helpers.create_response import create_response
import json
from django.db.utils import IntegrityError

class CustomResponseMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)        
        try:
            parseResponse,code = create_response(response.status_code,"Ok",json.loads(response.getvalue()),request.path,request.method)
            return HttpResponse(json.dumps(parseResponse),content_type="application/json",status=code)
        except (Exception,IntegrityError) as e:
            return HttpResponse("Unexpected error",status=400)
