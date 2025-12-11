from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ErrorDetail

from . import constant


def is_request_internal(renderer_context):
    if 'view' not in renderer_context:
        return False

    view = renderer_context.get('view')
    if hasattr(view, 'internal'):
        if view.internal:
            return True

    return False


def is_request_list(renderer_context):
    if 'view' not in renderer_context:
        return False

    view = renderer_context.get('view')
    if hasattr(view, 'paginator'):
        if not view.paginator:
            return False

    view = renderer_context.get('view')
    if hasattr(view, 'action'):
        return view.request.method == 'GET' and view.action == "list"
    return view.request.method == 'GET' and hasattr(view, 'list') and callable(getattr(view, 'list'))


# CustomRender class...
class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Not Custom if API is forwarder
        if is_request_internal(renderer_context):
            return super().render(data, accepted_media_type=None, renderer_context=None)

        status_code = renderer_context['response'].status_code
        response = {}
        if str(status_code).startswith('2'):
            # Not custom if list api
            if is_request_list(renderer_context):
                return super().render(data, accepted_media_type=None, renderer_context=None)

            response = {
                "success": True,
                "error_message": None,
                "error_code": None,
                "data": data
            }
        elif str(status_code).startswith('4'):
            if status_code == 401:
                response = constant.HTTP_RESPONSE_401
            elif status_code == 403:
                response = constant.HTTP_RESPONSE_403
            elif status_code == 404:
                response = constant.HTTP_RESPONSE_404
            else:
                code, messages = self.get_messages(data)
                if code == '' and len(messages) == 0:
                    print('[DEBUG] custom_response 400:', data)
                response["success"] = False
                response["error_message"] = messages
                response["error_code"] = code
                response["data"] = {}
        else:
            response = constant.HTTP_RESPONSE_500

        return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)

    @classmethod
    def get_messages(cls, data):
        code = ''
        messages = []
        print('[DEBUG] get_messages:', data)
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "err_code":
                    code = value
                elif key == "message":
                    if isinstance(value, list):
                        for message in value:
                            messages.append(message)
                    elif isinstance(value, str):
                        messages.append(value)
                elif isinstance(value, list):
                    if all(isinstance(item, ErrorDetail) for item in value):
                        messages.append(f"{key}: {value[0]}")
                    else:
                        for message in value:
                            messages.append(f"{key}: {message}")
                elif isinstance(value, ErrorDetail):
                    messages.append(f"{key}: {value}")
        elif isinstance(data, list):
            if all(isinstance(item, ErrorDetail) for item in data):
                messages.append(data[0])
            else:
                for message in data:
                    messages.append(message)
        elif isinstance(data, str):
            messages.append(data)
        return code, messages
