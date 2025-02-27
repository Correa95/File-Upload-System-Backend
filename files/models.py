from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=1024)
    upload_timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(default="default_file.pdf")
    
    def __str__(self):
        return self.name