from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import gettext_lazy as _


class CustomPaginator(Paginator):

    def validate_number(self, number):
        """Validate the given 1-based page number."""
        try:
            if isinstance(number, float) and not number.is_integer():
                raise ValueError
            number = int(number)
        except (TypeError, ValueError):
            raise PageNotAnInteger(_('That page number is not an integer'))
        if number < 1:
            raise EmptyPage(_('That page number is less than 1'))
        return number


class CustomPagination(pagination.PageNumberPagination):
    page_query_param = 'page_num'
    page_size_query_param = 'page_size'
    django_paginator_class = CustomPaginator

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page_size', self.page.paginator.per_page),
            ('page_num', self.page.number),
            ('count', self.page.paginator.count),
            ('has_next', self.page.has_next()),
            ('has_previous', self.page.has_previous()),
            ('data', data)
        ]))
