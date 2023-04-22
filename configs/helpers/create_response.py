from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict


def create_response(code, message, data, path='', method=""):
    """
    Function to create a response to be sent back via the API
    :param request_id:Id fo the request
    :param code:Error Code to be used
    :param message:Message to be sent via the APi
    :return:Dict with the above given params
    """

    data_parse = {'ok': False, "message": "",
                  "errors": "", "path": "", "method": "", "next": None, "previous": None, "count": None}

    try:

        if code != 200:
            proccess_data = data
            if type(data) is list and len(data) > 0:
                proccess_data = [ x for x in data][0]
            elif type(data) is dict:
                proccess_data = [{x: data[x][0]} for x in data]
            elif type(data) is ReturnDict:
                proccess_data = [{x: data[x]['non_field_errors'][0]
                                  if "non_field_errors" in data[x] else data[x][0]} for x in data]

            if type(proccess_data) is dict or type(proccess_data) is list:
                data_parse["errors"] = proccess_data
                data_parse["message"] = message
                data_parse["path"] = path
                data_parse["method"] = method
            else:
                data_parse["errors"] = proccess_data
                data_parse["message"] = message
                data_parse["path"] = path
                data_parse["method"] = method

            return data_parse, code

        data_parse["data"] = data if 'count' not in data else data["results"]
        data_parse["message"] = message
        data_parse["ok"] = True
        data_parse["path"] = path
        data_parse["method"] = method
        data_parse["next"] = None if "next" not in data else data["next"]
        data_parse["previous"] = None if "previous" not in data else data["previous"]
        data_parse["count"] = None if "count" not in data else data["count"]

        return data_parse, code
    except (Exception, BaseException) as creation_error:
        return Response({creation_error}, status=code)
