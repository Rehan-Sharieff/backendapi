from django.urls import path
from .views import ProtectedAPIView

urlpatterns = [
    path('protected/', ProtectedAPIView.as_view()),
]



