from django.urls import path

from .views import RegistroView, perfil_usuario

urlpatterns = [
    path('register/', RegistroView.as_view()),
    path('perfil/', perfil_usuario),
]