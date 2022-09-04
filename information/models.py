from django.db import models
from django.urls import reverse


# Create your models here.

class FamilyDetail(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="family/%Y/%m/%d")
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, null=True)

    class Meta:
        ordering = ['id']
        index_together = [['id','slug']]


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('information:family_detail', args=[self.id, self.slug])
