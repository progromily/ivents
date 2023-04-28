from django.urls import path, include

urlpatterns = [
    path('api/ivents/', include('ivents.urls')),
]
