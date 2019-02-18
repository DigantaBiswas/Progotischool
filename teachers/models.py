from django.db import models

# Create your models here.
class Teacher(models.Model):
	name = models.CharField(max_length=50)
	picture = models.ImageField(upload_to='teachers/')
	designation=models.CharField(max_length=100)
	contact = models.CharField(max_length=14,blank=True)
	bio = models.TextField(blank=True)
	join_date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name