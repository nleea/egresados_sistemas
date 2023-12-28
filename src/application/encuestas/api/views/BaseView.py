from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class BaseView(APIView):
    
    def get_meta(self):
        if "meta" in self.request.headers:
            return self.request.headers["meta"]
        return None
    
    @method_decorator(cache_page(60*60*2))
    def get(self,request,*args, **kwargs):
        pass
    
    def post(self,request,*args, **kwargs):
        pass
    
    def delete(self,request,*args, **kwargs):
        pass
    
    def put(self,request,*args, **kwargs):
        pass
