from django.db import models
from django.urls import reverse


# Create your models here.

class FamilyDetail(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    eng_title = models.CharField(max_length=100)
    kor_title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="family")
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, null=True)
    sub_title = models.CharField(max_length=100)
    sub_img = models.ImageField(upload_to="family/sub")
    appearance = models.CharField(max_length=5000)
    taste = models.CharField(max_length=5000)


    class Meta:
        ordering = ['id']
        index_together = [['id', 'slug']]


    def __str__(self):
        return self.eng_title

    def get_absolute_url(self):
        return reverse('information:family_detail', args=[self.slug])
