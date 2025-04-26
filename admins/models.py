from django.db import models

class UserRegisterTable(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)


from django.db import models

class RealEstateData(models.Model):
    posted_by = models.CharField(max_length=255)
    under_construction = models.IntegerField()
    rera = models.IntegerField()
    bhk_no = models.IntegerField()
    bhk_or = models.CharField(max_length=10)
    square_ft = models.FloatField()
    ready_to_move = models.IntegerField()
    resale = models.IntegerField()
    address = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    target_price = models.FloatField()
    is_approved = models.BooleanField(default=False)  # Approval field

    def __str__(self):
        return f"{self.posted_by} - {self.address}"