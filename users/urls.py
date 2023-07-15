from django.urls import path, include
from .views import RegisterView, logout, ProfileCreateView, ProfileUpdateView


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/logout/', logout),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileCreateView.as_view()),
    path('profile/<int:pk>/', ProfileUpdateView.as_view()),
]