from django.contrib import admin
from django.urls import path, include
from myapp.views import QRCodeAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('generate-qr/', QRCodeAPIView.as_view(), name='generate_qr'),
]
