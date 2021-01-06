from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.urls import reverse

class Post(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number or Mobilephone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    mobilephone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    address = models.TextField()

    def __str__(self):
        return self.name + ' | ' + str(self.user) 

    def get_absolute_url(self):
        return reverse('home')
                       