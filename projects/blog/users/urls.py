from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Import LoginView and LogoutView
from .views import RegisterView, LogoutView
from . import views



from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('logout/', views.CustomLogout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', LogoutView.as_view(), name='token_logout'),
]


