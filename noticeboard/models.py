from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify 
from .utils import get_unique_slug

import random 

# from progotischool.utils import unique_slug_generator
# Create your models here.
class Notice(models.Model):
	title = models.CharField(max_length=30)
	description = models.TextField(blank=True,null = True)
	attachment  = models.FileField(blank=True,null = True, upload_to='notification_files/')
	picture = models.ImageField(upload_to='images/',null = True, blank=True)
	upload_date = models.DateTimeField(auto_now_add=True)
	valid_till = models.DateTimeField()
	slug = models.SlugField(max_length=40,unique=True,blank=True)

	def __str__(self):
		return self.title

	# def _get_unique_slug(self):
	# 	slug = slugify(self.title)
	# 	unique_slug = slug
	# 	num = 1
	# 	while Notice.objects.filter(slug=unique_slug).exists():
	# 	    unique_slug = '{}-{}'.format(slug, num)
	# 	    num += 1
	# 	return unique_slug



	# def save(self, *args, **kwargs):
	# 	if not self.slug:
	# 	    self.slug = get_unique_slug(self, 'title', 'slug')
	# 	super().save(*args, **kwargs)





# def post_pre_save_receiver(instance,sender,*args,**kwargs):
 
#     if not instance.slug:
 
#         instance.slug=unique_slug_generator(instance)
 
 
# pre_save.connect(post_pre_save_receiver,sender=Notice)


	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = get_unique_slug(self,self.title, 'slug')
		super(Notice, self).save(*args, **kwargs)

