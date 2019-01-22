from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify 
from .utils import get_unique_slug


# Create your models here.
class Results(models.Model):
	result_of = models.CharField(max_length=100)
	file = models.FileField(blank=True, null = True, upload_to = 'result_files')
	upload_date = models.DateTimeField(auto_now = True)
	slug = models.SlugField(max_length=40,unique=True,blank=True,allow_unicode=True)

	def __str__(self):
		return self.result_of

	def save(self, *args, **kwargs):
		if not self.slug:
		    self.slug = get_unique_slug(self, 'result_of', 'slug')
		super().save(*args, **kwargs)
