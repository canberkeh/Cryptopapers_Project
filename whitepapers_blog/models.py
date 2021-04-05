from django.db import models
from django.contrib.auth.models import User


# Create your models here

#Whitepapers model 
class WhitePapers(models.Model):
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'WhitePapers'
        verbose_name_plural = 'WhitePapers'

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #additional - optional
    website = models.URLField(blank=True) #// zorunlu değil (blank true)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)  #//zorunlu değil 

    def __str__(self):
        return self.user.username