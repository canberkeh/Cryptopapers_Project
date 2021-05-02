from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime


class CoinRanking(models.Model):

    name = models.CharField(max_length=32)
    is_approved = models.BooleanField(default=False) # Adding currency by admin approval
    like = models.IntegerField(default = 0)
    dislike = models.IntegerField(default = 0)
    hodl = models.IntegerField(default = 0)
    total_points = models.IntegerField(default = 0)
        
    def __str__(self):
        return self.name

class Comments(models.Model):
    coin_name = models.ForeignKey(CoinRanking, on_delete=CASCADE)
    comment = models.TextField()
    like = models.IntegerField(default = 0)
    dislike = models.IntegerField(default = 0)
    create_date = models.DateTimeField(default=datetime.now(), blank=True)
    
    def str(self):
        return self.coin_name