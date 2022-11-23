from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from venue.models import Hangout

venue_select = []
for i in range(31, 83):
    venue_select.append((Hangout.objects.get(pk=i).__str__(), Hangout.objects.get(pk=i).__str__()[Hangout.objects.get(pk=i).__str__().find(':')+1:]))

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    venue = models.CharField(max_length=100, choices=venue_select)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})