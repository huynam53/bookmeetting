from django.urls import path, include
from api.v1 import router as api_v1
from api.v2 import router as api_v2

urlpatterns = [
    path('api/v1', include(api_v1)),
    path('api/v2', include(api_v2)),
]
