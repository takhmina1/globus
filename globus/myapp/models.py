from django.db import models
from django.db import models
from django.db import models
from django.core.files.base import ContentFile
import qrcode
from io import BytesIO



class User(models.Model):
    username = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"User: {self.username}")
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        filename = f"qr_code_{self.username}.png"
        self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)
        self.save()

    
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
   

   
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='orders')
    date_ordered = models.DateTimeField(auto_now_add=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

class History(models.Model):
    event = models.CharField(max_length=255)
    date = models.DateField()

class ShoppingCart(models.Model):
    product = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
