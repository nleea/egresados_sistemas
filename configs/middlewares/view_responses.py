from django.http import HttpResponse
from ..helpers.create_response import create_response
import json
from django.db.utils import IntegrityError
import re
from django.core.cache import cache
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG,format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

class CustomResponseMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)     
        try:
            decode = response.getvalue().decode()
            match = re.search(r'^[\d+]\s(.+)', decode)
            if response.status_code != 200:
                logging.warning(f"{decode}")
            if match or type(decode) is list and decode[0].isdigit():
                decode = ["".join(x) for x in decode]   
                parseResponse,code = create_response(response.status_code,"Ok",decode,request.path,request.method)
                return HttpResponse(json.dumps(parseResponse),content_type="application/json",status=code)
            if request.method in ["POST","PUT","DELETE"]:
                cache.clear()
            parseResponse,code = create_response(response.status_code,"Ok", decode,request.path,request.method)
            return HttpResponse(json.dumps(parseResponse),content_type="application/json",status=code)
        except (Exception,IntegrityError) as e:
            logging.warning(f"{e}")
            return HttpResponse("Unexpected error",status=400)
    
    
    def process_exception(self,request,exception):
        return HttpResponse(exception)
