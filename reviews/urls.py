from django.urls import path

from reviews.apps import ReviewsConfig
from reviews.views import ReviewCreateApiView, ReviewListApiView, ReviewUpdateApiView, ReviewDestroyApiView

app_name = ReviewsConfig.name

urlpatterns = [
    path('create/<ad_pk>/', ReviewCreateApiView.as_view(), name='review_create'),
    path('list/', ReviewListApiView.as_view(), name='review_list'),
    path('update/<int:pk>/', ReviewUpdateApiView.as_view(), name='review_update'),
    path('delete/<int:pk>/', ReviewDestroyApiView.as_view(), name='review_delete'),
]
