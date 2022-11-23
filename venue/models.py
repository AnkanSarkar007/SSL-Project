from django.db import models

class Hangout(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=10, default='hotel')
    rate = models.DecimalField(default=0, decimal_places=1, max_digits=5)
    total = models.DecimalField(default=0, decimal_places=1, max_digits=5)
    rating = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    
    def __str__(self):
        s = str(self.id) + ':' + self.title + ', ' + self.location
        return s