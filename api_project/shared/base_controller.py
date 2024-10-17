from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BaseController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._message = ""
        self._code = status.HTTP_200_OK

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message

    def get_code(self):
        return self._code

    def set_code(self, code):
        self._code = code

    def respond(self, data, headers=None):
        headers = headers or {}
        return Response(data, status=self.get_code(), headers=headers)

    def respond_with_error(self, message='', errors=None, code=status.HTTP_422_UNPROCESSABLE_ENTITY):
        self.set_code(code)
        return self.respond({
            'message': message,
            'data': None,
            'errors': errors or [],
            'success': False,
            'status_code': self.get_code(),
        })

    def respond_with_data(self, message=None, data=None, success=True):
        self.set_code(status.HTTP_200_OK)
        return self.respond({
            'data': data,
            'message': message,
            'success': success,
            'status_code': self.get_code()
        })

    def respond_with_token(self, message, token):
        self.set_code(status.HTTP_201_CREATED)
        return self.respond({
            'message': message,
            'token': token,
            'token_type': 'Bearer',
            'success': True,
            'status_code': self.get_code()
        })

    def respond_http_bad_request(self, message='Bad Request'):
        self.set_code(status.HTTP_400_BAD_REQUEST)
        return self.respond_with_error(message)

    def respond_http_unauthorized(self, message='Unauthorized'):
        self.set_code(status.HTTP_401_UNAUTHORIZED)
        return self.respond_with_error(message)

    def respond_http_conflict(self, message='Data Conflict'):
        self.set_code(status.HTTP_409_CONFLICT)
        return self.respond_with_error(message)

    def respond_unprocessable_entity(self, message='Unprocessable Entity'):
        self.set_code(status.HTTP_422_UNPROCESSABLE_ENTITY)
        return self.respond_with_error(message)
