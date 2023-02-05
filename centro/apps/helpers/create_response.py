from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict


def create_response(code, message, data, request_id='',):
    """
    Function to create a response to be sent back via the API
    :param request_id:Id fo the request
    :param code:Error Code to be used
    :param message:Message to be sent via the APi
    :return:Dict with the above given params
    """

    try:
        req = str(request_id)
        if code != 200:
            proccess_data = data
            if type(data) is list and len(data) > 0:
                proccess_data = [{x: data[x][0]} for x in data][0]
            if type(data) is dict:
<<<<<<< HEAD
                proccess_data = [{x: data[x]} for x in data][0]
            if type(data) is ReturnDict:
                proccess_data = [{x: data[x]['non_field_errors'][0] if "non_field_errors" in data[x]  else data[x][0]} for x in data][0]
            data_parse = {'ok': False, "message":message,"errors": {
=======
                proccess_data = [{x: data[x][0]} for x in data][0]
            if type(data) is ReturnDict:
                proccess_data = [{x: data[x]['non_field_errors'][0] if "non_field_errors" in data[x]  else data[x][0]} for x in data][0]
            data_parse = {'ok': False, "errors": {
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
                'error': proccess_data}, "request_id": req}
            return data_parse, code

        data_parse = {'ok': True,
<<<<<<< HEAD
                      'message':message,
=======
>>>>>>> 685e7b097d6b83089baa1a651f6855eae9e73db5
                      'data': data, "request_id": req}
        return data_parse, code
    except Exception as creation_error:
        return Response({creation_error}, status=code)
