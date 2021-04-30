from django.db import models

class CoinRanking(models.Model):

    name = models.CharField(max_length=32)
    is_approved = models.BooleanField(default=False) # Adding currency by admin approval
    like = models.IntegerField(default = 0)
    dislike = models.IntegerField(default = 0)
    hodl = models.IntegerField(default = 0)
    total_points = models.IntegerField(default = 0)
        
    def __str__(self):
        return self.name
