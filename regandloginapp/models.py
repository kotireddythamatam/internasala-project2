from django.db import models
class Regmodel(models.Model):
    user_name=models.CharField(primary_key=True, max_length=20)
    password=models.CharField(max_length=15)
    conform_password=models.CharField(max_length=15)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    mobile_number=models.IntegerField()
    email_id=models.EmailField()
