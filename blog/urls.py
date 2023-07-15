from django.urls import path
from rest_framework import routers
from .views import (
    CommentView,
    BlogViewset,
    LikeView,
)


router =routers.DefaultRouter()
router.register('', BlogViewset)
urlpatterns = [
    path('comment/', CommentView.as_view(), name='comment'),
    path("like/<str:slug>/", LikeView.as_view())
] + router.urls