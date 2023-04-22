from django.http import HttpResponse
from apps.auth_module.models import Resources
from ..helpers.create_response import create_response
import json
from django.db.utils import IntegrityError
import re

class CustomResponseMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)        
        try:
            decode = response.getvalue().decode()
            match = re.search(r"\((\d+)", decode)
            if match:
                text = decode.split(",")    
                decode = text[1] + text[2]
                parseResponse,code = create_response(response.status_code,"Ok",decode,request.path,request.method)
                return HttpResponse(json.dumps(parseResponse),content_type="application/json",status=code)
            
            parseResponse,code = create_response(response.status_code,"Ok",json.loads(decode),request.path,request.method)
            return HttpResponse(json.dumps(parseResponse),content_type="application/json",status=code)
        except (Exception,IntegrityError) as e:
            return HttpResponse("Unexpected error",status=400)
    
    
    def process_exception(self,request,exception):
        return HttpResponse(exception)



    def process_view(self,request,view_func,*args, **kwargs):
        return view_func(request)