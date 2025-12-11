import uuid

from django.db import models

from .manager import BaseManager, BaseUuidManager


def default_created_by():
    return {'email': 'system@hana.com'}


def anonymous_information():
    return {"email": "anonymous@hana.com"}


def get_uuid_string():
    return str(uuid.uuid4())


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.JSONField(default=default_created_by, blank=True, null=True)
    updated_by = models.JSONField(default=default_created_by, blank=True, null=True)

    objects = BaseManager()

    class Meta:
        abstract = True


class BaseUuidModel(BaseModel):
    id = models.CharField(max_length=36, primary_key=True, default=get_uuid_string)

    objects = BaseUuidManager()

    class Meta:
        abstract = True


class UserInfo:
    id: int = None
    firstname: str = ""
    lastname: str = ""
    username: str = ""
    email: str = None
    avatar: str = None
    is_superuser: bool = False
    is_staff: bool = False

    partner_id: int = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def get_full_name(self):
        full_name = '%s %s' % (self.firstname, self.lastname)
        return full_name.strip()

    def to_dict_base(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.firstname,
            'last_name': self.lastname,
        }

