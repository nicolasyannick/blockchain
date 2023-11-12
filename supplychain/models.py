from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('ordered', 'Ordered'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ordered')

    def __str__(self):
        return f"Order of {self.product.name} on {self.order_date}"

