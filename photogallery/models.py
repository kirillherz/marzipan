from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

class CakeModel(models.Model):
	name = models.CharField(max_length = 40, verbose_name = 'Название')
	description = models.CharField(max_length = 40, verbose_name = 'Описание')
	weight = models.FloatField(verbose_name = 'Вес')
	macrobiotic_value = models.FloatField(verbose_name = 'Энергитическая ценность')
	cost = models.FloatField(verbose_name = 'Стоимость')
	image = models.FileField(upload_to = 'cakes', verbose_name = 'Изображение')
	
	class Meta:
		verbose_name = 'Торт'
		verbose_name_plural = 'Торты'
		
	def __str__(self):
		return self.name

class FeedbackModel(models.Model):
	name = models.CharField(max_length = 40, verbose_name = 'Имя')
	e_mail = models.EmailField(blank = True)
	phone_number = models.IntegerField(validators = [RegexValidator("[0-9]{10}", "Incorrectly phone number" )])
	message = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.name
	
class ReviewModel(models.Model):
	name = models.CharField(max_length = 40, verbose_name = 'Имя')
	cake = models.ForeignKey(CakeModel)
	review = models.CharField(max_length = 100)
	rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
	
	class Meta:
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'
		
	def __str__(self):
		return self.name
	

	