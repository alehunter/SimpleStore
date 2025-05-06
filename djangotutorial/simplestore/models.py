from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    name = models.CharField(max_length=300)
    defaultPrice = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        output = "Customer: "+ self.customer.name + " - Order Number: " + str(self.id)
        return output


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete= models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        output = "Order: " + str(self.order.id) + ", Item: " + self.item.name + ", Price: " + str(self.item.defaultPrice) + ", Quantity: " + str(self.quantity)
        return output

