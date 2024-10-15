from django.db import models
from django.contrib.auth.models import User 



class Property(models.Model):
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    home_type = models.CharField(max_length=25)
    year_built = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')  # link to User
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}"

class Appliance(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='appliances')
    exp_end_of_life = models.DateField()
    purchase_date = models.DateField()
    current_status = models.CharField(max_length=20) #
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.model})"
    
class Repairs(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, related_name='repairs')
    repair_date = models.DateField()
    repaired_by = models.CharField(max_length=250)
    repaired_description = models.CharField(max_length=250)
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Investments(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, related_name='investments')  # Use ForeignKey
    investment_type = models.CharField(max_length=25)
    investment_date = models.DateField()
    investment_description = models.CharField(max_length=250)
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

