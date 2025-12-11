from enum import Enum


class EnumStatic(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def value_choices(cls):
        return list(i.value for i in cls)

    @classmethod
    def to_dict(cls):
        return dict((i.value, i.name) for i in cls)
