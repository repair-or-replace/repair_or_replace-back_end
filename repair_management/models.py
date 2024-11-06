from django.db import models
from django.contrib.auth.models import User 
from datetime import timedelta


#models define the data structure of the app. they represent the tabels in your DB and define the fields and relationship between them
#django uses models to generate SQL code to create and manipulate the corresponding DB tables


class ApplianceApi(models.Model):
    brand = models.CharField(max_length=50,null=True) #brand_name
    model = models.CharField(max_length=100,null=True) #sku
    description = models.CharField(max_length=250,null=True) #name of item
    category_name = models.CharField(max_length=50,null=True)
    detail_category_name = models.CharField(max_length=250, null=True)
    color = models.CharField(max_length=30,null=True)
    product_image = models.CharField(max_length=250, null=True)
    product_doc_1 = models.CharField(max_length=250, null=True)
    product_doc_2 = models.CharField(max_length=250, null=True)
    lowest_listed_price = models.DecimalField(max_digits=10, decimal_places=2)
    home_depot_price = models.DecimalField(max_digits=10, decimal_places=2)
    msrp = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.brand} {self.model}"

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
    year_built = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')  # link to User
    default_image = models.CharField(max_length=250, default='images/default_home_pic.jpeg')
    user_uploaded_image = models.ImageField(upload_to='properties/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}"
    
    def image(self):
        if self.user_uploaded_image:
            return self.user_uploaded_image.url
        return f'images/default_home_pic.jpeg'
    

class Appliance(models.Model):
    STATUS_CHOICES = [
        ('working', 'Working'),
        ('needs repair', 'Needs Repair'),
        ('broken', 'Broken'),
        ('replaced', 'Replaced')
    ]
    name = models.CharField(max_length=255, default='default_name')
    appliance_type = models.CharField(max_length=200)
    brand = models.CharField(max_length=200,blank=True)
    model = models.CharField(max_length=200,null=True,blank=True)
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='appliances')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appliances') 
    exp_end_of_life = models.DateField(blank=True,null=True)
    purchase_date = models.DateField()
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICES) #
    cost = models.FloatField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    typical_lifespan_years = models.IntegerField(default=10)  # e.g., average lifespan in years

    def expected_end_of_life(self):
        """Calculates the expected end-of-life date for the appliance."""
        return self.purchase_date + timedelta(days=self.typical_lifespan_years * 365)

    def __str__(self):
        return f"{self.name} ({self.model})"
    
class Repairs(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, related_name='repairs')
    repair_date = models.DateField()
    repaired_by = models.CharField(max_length=250)
    repaired_description = models.CharField(max_length=250)
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='repairs')  # link to User


    def __str__(self):
        return f"{self.appliance} ({self.repair_date})"

class Investments(models.Model):
    INVESTMENT_CHOICES = [
        ('maintenance', 'Maintenance'),
        ('enhancement', 'Enhancement')
    ]
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, related_name='investments')  # Use ForeignKey
    investment_type = models.CharField(max_length=25, choices=INVESTMENT_CHOICES)
    investment_date = models.DateField()
    investment_description = models.CharField(max_length=250)
    cost = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investments')  # link to User


    def __str__(self):
        return f"{self.appliance} ({self.investment_type})"
    