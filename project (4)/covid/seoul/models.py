from django.db import models


class Vaccine(models.Model):
    location = models.CharField(max_length=30, primary_key=True)
    # vaccineCnt = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    month7 = models.IntegerField(default=0)
    month8 = models.IntegerField(default=0)
    month9 = models.IntegerField(default=0)
    month10 = models.IntegerField(default=0)
    
    def __str__(self):
        return self.location