from django.db import models
from django.core.validators import MaxValueValidator

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    BookingDate = models.DateTimeField

    def __str__(self):
        return self.Name
    
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(validators=[MaxValueValidator(5)])

    def get_item(self):
        return f'{self.Title} : {str(self.Price)}'
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'