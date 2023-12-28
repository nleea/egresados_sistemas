from rest_framework.views import APIView
from ...serializers.pagination.Pagination import CustomPagination
from rest_framework.response import Response
from rest_framework import status


class ViewPagination(APIView):
    pagination_class = CustomPagination

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class DecoratorPaginateView(ViewPagination, object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.request = args[0]
        response = self.func(request=self.request, *args, **kwargs)

        resulst = self.paginate_queryset(response)
        paginate_data = self.get_paginated_response(resulst).data

        if paginate_data is None:
            return Response("error", status.HTTP_400_BAD_REQUEST)

        return Response(paginate_data, status.HTTP_200_OK)
