from django.shortcuts import render
from rest_framework import generics
from .models import User, Product, Order
from .serializers import UserSerializer, ProductSerializer, OrderSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import qrcode
from PIL import Image
from rest_framework import generics
from .models import ProductCategory, History, ShoppingCart
from .serializers import ProductCategorySerializer, HistorySerializer, ShoppingCartSerializer



class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response({'user_id': user.id, 'qr_code_url': user.qr_code.url}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = serializer.save()
        user.generate_qr_code()
        return user
# Assuming you have the qrcode and Pillow libraries installed


def generate_qr_code_with_logo(data, logo_path, output_path):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Open and resize the logo image
    # logo_img = Image.open(logo_path)
    logo_size = (qr_img.size[0] // 4, qr_img.size[1] // 4)
    logo_img = logo_img.resize(logo_size, Image.ANTIALIAS)

    # Paste the logo onto the QR code
    position = ((qr_img.size[0] - logo_size[0]) // 2, (qr_img.size[1] - logo_size[1]) // 2)
    qr_img.paste(logo_img, position)

    # Save the final QR code with the logo
    qr_img.save(output_path)

# Example usage:
data_for_qr_code = "Your Registration Data"
telegram_logo_path = "path/to/telegram_logo.png"  # Provide the path to the Telegram logo image
output_qr_code_path = "path/to/output_qr_code.png"  # Specify the desired output path for the QR code
# generate_qr_code_with_logo(data_for_qr_code, telegram_logo_path, output_qr_code_path)


import qrcode
from io import BytesIO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


class QRCodeAPIView(APIView):
    def get(self, request):
        # Получите ссылку из запроса (здесь предполагается, что ссылка передается в параметре 'url')
        url = request.query_params.get('url', 'generate-qr/')

        # Проверка наличия ссылки
        if not url:
            return Response({'error': 'Параметр "url" отсутствует в запросе.'}, status=status.HTTP_400_BAD_REQUEST)

        # Создание QR-кода
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Генерация изображения QR-кода
        img = qr.make_image(fill_color="black", back_color="white")

        # Сохранение изображения в байтовом потоке
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        # Отправка изображения в ответе API
        return HttpResponse(buffer, content_type='image/png')
    
    
    
    
    

class ProductCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class HistoryListCreateView(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class HistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class ShoppingCartListCreateView(generics.ListCreateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class ShoppingCartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
