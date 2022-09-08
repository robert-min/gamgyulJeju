from django.db import models

# Create your models here.
class ActivityMap(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    place = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    period = models.CharField(max_length=200, null=True)
    how = models.CharField(max_length=50, null=True)
    website = models.CharField(max_length=100, null=True)
    lat = models.IntegerField(null=True)
    long = models.IntegerField(null=True)

    class Meta:
        ordering = ['id']
        index_together = [['id', 'place']]

    def __str__(self):
        return self.place