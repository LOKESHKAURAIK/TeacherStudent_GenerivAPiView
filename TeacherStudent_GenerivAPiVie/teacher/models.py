from django.db import models

class Teacher(models.Model):
    tname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.tname
    