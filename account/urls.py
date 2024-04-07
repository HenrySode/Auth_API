from django.urls import path
from . import views

urlpatterns = [
    #user path
    path('users/', views.UserListCreate.as_view(), name='users'),
    path('users/<str:pk>', views.UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    
    #profile path
    path('profiles/', views.ProfileListCreate.as_view(), name='profiles'),
    path('profiles/<str:pk>', views.ProfileRetrieveUpdateDestroy.as_view(), name='profile-detail'),
    
    #login path
    path('login/', views.LoginApiView.as_view(), name='login'),
]