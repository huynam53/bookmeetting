from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import generics, filters, status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response

from app.core import mixins
from configs.handle_response import CustomRenderer, CustomPagination


class BaseAPIView(generics.GenericAPIView, mixins.BaseMixin):
    pass


class BaseListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    pagination_class = CustomPagination
    search_fields = []
    filterset_fields = []
    ordering = []


class BaseCreateAPIView(generics.CreateAPIView, BaseAPIView, mixins.BasePrepareDataMixin):
    permission_classes = (AllowAny,)
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    def post(self, request, *args, **kwargs):
        request = self.prepare_data()
        return super().post(request, *args, **kwargs)


class BaseListCreateAPIView(BaseListAPIView, BaseCreateAPIView):
    pass


class BaseRetrieveAPIView(generics.RetrieveAPIView, BaseAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class BaseUpdateAPIView(generics.UpdateAPIView, BaseAPIView, mixins.BasePrepareDataMixin):
    permission_classes = (AllowAny,)
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    def put(self, request, *args, **kwargs):
        request = self.prepare_data()
        return super().put(request, *args, **kwargs)


class BaseDestroyAPIView(generics.DestroyAPIView, BaseAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(status=status.HTTP_200_OK)

    def soft_destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_200_OK)


class BaseRetrieveDestroyAPIView(BaseRetrieveAPIView, BaseDestroyAPIView):
    pass
