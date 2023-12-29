from django.db import models

# Create your models here.

class Cities(models.Model):
    city_id = models.IntegerField(primary_key = True)
    city = models.CharField(max_length=200, null= False)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['city'], name='unique_city_name')
        ]
        db_table = 'cities'