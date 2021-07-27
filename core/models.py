from django.db import models

# Create your models here.

class User(models.Model):
    
    first_name = models.CharField(("First Name"), max_length=50)
    last_name = models.CharField(("Last Name"), max_length=50)
    

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    


    