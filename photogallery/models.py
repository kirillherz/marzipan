from django.db import models

class CakeModel(models.Model):
	name = models.CharField(max_length = 40,verbose_name='Название')
	description = models.CharField(max_length = 40,verbose_name='Описание')
	cost = models.FloatField(verbose_name='Стоимость')
	image = models.FileField(upload_to='cakes',verbose_name='Изображение')
	
	class Meta:
		verbose_name = 'Торт'
		verbose_name_plural = 'Торты'
		
	def __str__(self):
		return self.name
		