from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField('full name', max_length=60)
    email=models.EmailField('email id', max_length=254)
    contact_no=models.IntegerField(max_length=10)
    reason=models.TextField('reason')
   
    
    def __str__(self):
        return self.email