from rest_framework.exceptions import ValidationError

from configs import error_code
from ..models import UserInfo


class BaseMixin:
    request = None
    serializer_class = None
    kwargs = None

    def get_user(self) -> UserInfo:
        user = self.request.user_info
        if not user:
            raise ValidationError(error_code.USER_MISSING_IN_TOKEN)
        return self.request.user_info

    def get_user_id(self):
        user = self.get_user()
        return user.id


class BasePrepareDataMixin:
    request = None
    kwargs = None
    
    def prepare_data(self):
        return self.request
