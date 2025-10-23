from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    create_at = models.DateField(auto_now_add=True)