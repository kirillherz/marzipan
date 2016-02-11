from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

class CakeModel(models.Model):
    name = models.CharField(max_length = 40, verbose_name = 'Название')
    description = models.CharField(max_length = 40, verbose_name = 'Описание')
    weight = models.FloatField(verbose_name = 'Вес')
    macrobiotic_value = models.FloatField(verbose_name = 'Энергитическая ценность')
    cost = models.FloatField(verbose_name = 'Стоимость')
    image = models.ImageField(upload_to = 'cakes', verbose_name = 'Изображение')

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'

    def __str__(self):
        return self.name

class FeedbackModel(models.Model):
    name = models.CharField(max_length = 40, verbose_name = 'Имя')
    e_mail = models.EmailField(blank = True)
    phone_number = models.IntegerField(verbose_name = 'Телефонный номер', validators = [RegexValidator("[0-9]{10}", "Incorrectly phone number" )])
    message = models.CharField(max_length = 200, verbose_name = 'Сообщение')

    def __str__(self):
        return self.name
        
class ReviewModel(models.Model):
    name = models.CharField(max_length = 40, verbose_name = 'Имя')
    cake = models.ForeignKey(CakeModel, verbose_name = 'Торт')
    review = models.CharField(max_length = 100, verbose_name = 'Отзыв')
    rating = models.IntegerField(verbose_name = 'Оценка', validators=[MinValueValidator(0),MaxValueValidator(5)])
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        
    def __str__(self):
        return self.name