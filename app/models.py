from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    subject = models.CharField(max_length=55)
    text = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
