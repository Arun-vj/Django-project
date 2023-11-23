from django.db import models

# Create your models here.
class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    status = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")
    