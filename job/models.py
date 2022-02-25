from django.db import models
from django.contrib.auth.models import User
# from decimal import Decimal

# from payments import PurchasedItem
# from payments.models import BasePayment
# Create your models here.

# class Payment(BasePayment):

#     def get_failure_url(self):
#         return self.user.username

#     def get_success_url(self):
#         return self.user.username

#     def get_purchased_items(self):
#         # you'll probably want to retrieve these from an associated order
#         yield PurchasedItem(name='Job Application Fee', sku='BSKV',
#                             quantity=1, price=Decimal(50), currency='INR')
    
class StudentUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=15,null=True)
    def _str_(self):
        return self.user.username



class Recruiter(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=10,null=True)
    company=models.CharField(max_length=50,null=True)
    type=models.CharField(max_length=15,null=True)
    status=models.CharField(max_length=20,null=True)
    def _str_(self):
        return self.user.username
    
    
class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    salary = models.FloatField(max_length=20)
    image = models.FileField()
    description = models.CharField(max_length=300)
    experience = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()
    def _str_(self):
        return self.title
    

    
    
    
class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser,on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    applydate = models.DateField()
    def _str_(self):
        return self.id