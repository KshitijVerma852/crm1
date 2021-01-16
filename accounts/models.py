from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.id})"


class Tag(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200, null=True)

class Product(models.Model):
    def __str__(self):
        return self.name
    CATEGORY = (
        ("Indoor", "Indoor"),
        ("Out door", "Out door")
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY, blank=True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

class Order(models.Model):
    STATUS = ( 
        ("Pending", "Pending"),
        ("Out for delivery", "Out for delivery"),
        ("Delivered", "Delivered")
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)


