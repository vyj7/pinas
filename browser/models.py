import random
from django.db import models
from jsonfield import JSONField
class uidgen:
    t=0;
    def uidchange(self):
        x=2**30
        y=2**40
        self.t=random.randint(x,y);
newuid=uidgen()
class SignUp(models.Model):
    full_name = models.CharField(max_length=120, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=10, blank=False)
    auth = models.BooleanField(blank=True,default=False)
    maxno = models.PositiveIntegerField(blank=True,default='0')
    uid = models.BigIntegerField(blank=True,default=newuid.t)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False,null=True)
    data = JSONField(null=True)
    #updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.full_name

class LogIn(models.Model):
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=10, blank=False)
    #updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.email
    

    
