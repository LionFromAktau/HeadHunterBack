from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls.v1')),
    path('api/', include('user.urls.v1')),
]

