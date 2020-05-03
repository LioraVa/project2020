from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Medical_Institutes(models.Model):
    Institute = models.CharField(max_length=100)
    city = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    address = models.ForeignKey(User, on_delete=models.CASCADE)
    # phone = models.ForeignKey(User, on_delete=models.CASCADE)

    # date_posted = models.DateTimeField(auto_now_add=True)

    # Institute':' 'city':    'phone':    'date_posted
    # title':'     'author':  'content':  'date_posted