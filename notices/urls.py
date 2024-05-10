from django.urls import path

from notices.apps import NoticesConfig
from notices.views import NoticesListApiView, NoticesCreateApiView, NoticesUpdateApiView, NoticesRetrieveApiView, \
    NoticesDestroyApiView, UserNoticesListApiView

app_name = NoticesConfig.name

urlpatterns = [
    path('', NoticesListApiView.as_view(), name='notices_list'),
    path('create/', NoticesCreateApiView.as_view(), name='notices_create'),
    path('update/<int:pk>/', NoticesUpdateApiView.as_view(), name='notices_update'),
    path('detail/<int:pk>/', NoticesRetrieveApiView.as_view(), name='notices_detail'),
    path('delete/<int:pk>/', NoticesDestroyApiView.as_view(), name='notices_delete'),
    path('me_list/', UserNoticesListApiView.as_view(), name='notices_list'),
]
