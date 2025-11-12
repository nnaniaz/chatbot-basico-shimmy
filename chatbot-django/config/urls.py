from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from chatbot.views import ChatbotView, ChatbotDetailView, DocumentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='login_de_usuario'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refrescar_token'),
    path('api/chatbot/', ChatbotView.as_view(), name='chatbot_view'),
    path('api/chatbot/<int:pk>/', ChatbotDetailView.as_view(), name='chatbot_detail_view'),
    path('api/document/', DocumentView.as_view(), name='document_view'),
]
