from django.urls import path
from .views import SignUpView, EditView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit/', EditView.as_view(), name='edit_profile'),
]
