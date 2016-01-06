from django.contrib import admin
from .models import CakeModel, ReviewModel, FeedbackModel

admin.site.register(CakeModel)
admin.site.register(ReviewModel)
admin.site.register(FeedbackModel)

