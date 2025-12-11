from rest_framework import serializers

from .models import BaseModel
from .models import UserInfo


class BaseSerializer(serializers.Serializer):
    class Meta:
        model = BaseModel
        fields = [
            'created_at',
            'updated_at',
            'created_by',
            'updated_by'
        ]
        abstract = True

    def set_created_by(self, data):
        user_info = self.context['request'].user_info.to_dict_base()

        if not self.instance:
            data['created_by'] = user_info
            data['updated_by'] = user_info
        else:
            data['updated_by'] = user_info


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = [
            'created_at',
            'updated_at',
            'created_by',
            'updated_by'
        ]
        abstract = True
        lower_case_fields = []

    def to_lower_case(self, data):
        if hasattr(self.Meta, 'lower_case_fields') and len(self.Meta.lower_case_fields):
            for field in self.Meta.lower_case_fields:
                if field in data and isinstance(data[field], str):
                    data[field] = data[field].lower()

        return data

    def to_internal_value(self, data):
        data = self.to_lower_case(data)
        return super().to_internal_value(data)

    def create(self, validated_data):
        user_info = self.get_user_info().to_dict_base()
        validated_data['created_by'] = user_info
        validated_data['updated_by'] = user_info
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user_info = self.get_user_info().to_dict_base()
        validated_data['updated_by'] = user_info
        return super().update(instance, validated_data)

    def get_user_info(self) -> UserInfo:
        user_info = self.context['request'].user_info
        return user_info


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    default_fields = []

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', self.default_fields)
        is_show_all = kwargs.pop('is_show_all', False)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if not is_show_all and fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
