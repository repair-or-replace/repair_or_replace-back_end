from django.db import models
from django.contrib.auth.models import User 

#models define the data structure of the app. they represent the tabels in your DB and define the fields and relationship between them
#django uses models to generate SQL code to create and manipulate the corresponding DB tables


class Property(models.Model):
    HOME_TYPE_CHOICES = [
        ('single', 'Single Family'),
        ('multi', 'Multi Family'),
        ('condo', 'Condo'),
        ('apartment', 'Apartment'),
        ('other', 'Other')
    ]

    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    home_type = models.CharField(max_length=25, choices=HOME_TYPE_CHOICES)
    year_built = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')  # link to User
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}"

class Appliance(models.Model):
    STATUS_CHOICES = [
        ('working', 'Working'),
        ('needs repair', 'Needs Repair'),
        ('broken', 'Broken'),
        ('replaced', 'Replaced')
    ]
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='appliances')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appliances') 
    exp_end_of_life = models.DateField()
    purchase_date = models.DateField()
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICES) #
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

    def __str__(self):
        return f"{self.appliance} ({self.repair_date})"

class Investments(models.Model):
    INVESTMENT_CHOICES = [
        ('replacement', 'Replacement'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
        ('upgrade', 'Upgrade')
    ]
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, related_name='investments')  # Use ForeignKey
    investment_type = models.CharField(max_length=25, choices=INVESTMENT_CHOICES)
    investment_date = models.DateField()
    investment_description = models.CharField(max_length=250)
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.appliance} ({self.investment_type})"


class ApplianceDetailsFromAPI(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"ApplianceDetailsFromAPI for {self.appliance} at {self.created_at}"

class CustomUser(models.Model):

    username = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    name = models.CharField(max_length=100)
    property_id = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"CustomUser {self.id}: {self.username}"


'''
class CustomUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    name = models.CharField(max_length=100)
    property_id = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField()
    # link User model
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"CustomUser {self.id}: {self.username}"

'''
