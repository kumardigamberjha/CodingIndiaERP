from django.db import models

class Requisition(models.Model):
    name = models.CharField(max_length=35)
    item = models.CharField(max_length = 35)
    qty = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    desc =  models.CharField(max_length=35, null = True, blank= True)
    
    def __str__(self):
        return self.item