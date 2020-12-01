from django.contrib import admin
from asgard_mvc.models import UserProfileModel, QuizModel, QuizEntryModel

# Register your models here.
admin.site.register(UserProfileModel)
admin.site.register(QuizModel)
admin.site.register(QuizEntryModel)