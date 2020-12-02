from django.contrib import admin
from asgard_mvc.models import UserProfileModel, QuizModel, QuizEntryModel, ARModel

# Register your models here.
admin.site.register(UserProfileModel)
admin.site.register(QuizModel)
admin.site.register(QuizEntryModel)
admin.site.register(ARModel)