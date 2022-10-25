from rest_framework.response import Response


def create_response(code, message, request_id='',):
    """
    Function to create a response to be sent back via the API
    :param request_id:Id fo the request
    :param code:Error Code to be used
    :param message:Message to be sent via the APi
    :return:Dict with the above given params
    """

    try:
        req = str(request_id)
        code = code
        data = {"data": message, "request_id": req}
        return data, code
    except Exception as creation_error:
        return Response({creation_error}, status=code)
