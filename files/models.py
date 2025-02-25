from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=1024)
    upload_timestamp = models.DateTimeField(auto_now_add=True,null=True)
    file = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.name