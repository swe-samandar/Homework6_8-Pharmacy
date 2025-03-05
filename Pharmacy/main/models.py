from django.db import models

# Create your models here.

class Medication(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    prescription_medications = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    manufactured_date = models.DateField()
    weight = models.IntegerField()
    description = models.TextField()
    expired_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/', blank=True, default=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'medication'

    def __str__(self):
        return f"{self.title} ({self.weight}mg)"