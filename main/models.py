import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu'),
        ('deker', 'Deker'),
        ('bola', 'Bola'),
        ('jersey', 'Jersey'),
        ('glove', 'Glove'),
        ('kaosKaki', 'KaosKaki'),
    ]
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField()

    def format_rupiah(self):
        return "Rp{:,.0f}".format(self.price).replace(",", ".")
    