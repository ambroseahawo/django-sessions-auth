from django.urls import path
from .views import GetUserProfileView, UpdateUserProfileView

app_name = "user_profiles"

urlpatterns = [
    path('user', GetUserProfileView.as_view()),
    path('update', UpdateUserProfileView.as_view()),
]