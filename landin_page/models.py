from django.db import models

# Create your models here.
class Homepage_content(models.Model):
	name = models.CharField(max_length=30)
	slide_pic1 =models.ImageField(upload_to='slides_images/')
	slide_pic2 =models.ImageField(upload_to='slides_images/')
	slide_pic3 =models.ImageField(upload_to='slides_images/')

	welcome_image = models.ImageField(upload_to='slides_images/')

	first_block_h1 = models.CharField(max_length=50,default=0)
	first_block_p = models.TextField(default=0)

	second_block_link = models.URLField(default=0)
	

	def __str__(self):
		return self.name