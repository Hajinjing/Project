from django.db import models

# Create your models here.
class Member(models.Model):
    m_id  = models.CharField(primary_key=True,max_length=100)
    m_pw = models.CharField(max_length=30)
    m_name = models.CharField(max_length=30)

    def __str__(self):
        return self.m_name