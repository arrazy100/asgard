from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver

from asgard import settings
import os, shutil, xlrd

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.username, filename)

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Hanya support file .jpg, .png, dan .gif')

def validate_quiz_file(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.xls', '.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Hanya support file .xls dan .xlsx')

# Create your models here.
class UserProfileModel(models.Model):
    username = models.CharField(max_length=100)
    image_profile = models.ImageField(upload_to=user_directory_path, validators=[validate_file_extension])
    current_level = models.IntegerField(default=1)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileModel.objects.create(username=instance.username, image_profile='marmut.jpg')

def delete_user_profile(sender, instance, *args, **kwargs):
    try:
        user = UserProfileModel.objects.get(username=instance.username)
        user.delete()
        dir = os.path.join(settings.MEDIA_ROOT, 'user_{0}'.format(user.username))
        shutil.rmtree(dir)
    except UserProfileModel.DoesNotExist:
        pass

signals.post_save.connect(receiver=create_user_profile, sender=User)
signals.post_delete.connect(receiver=delete_user_profile, sender=User)

class QuizEntryModel(models.Model):
    level = models.IntegerField(default=1)
    nomor = models.IntegerField(default=1)
    soal = models.TextField()
    jawaban_a = models.TextField()
    jawaban_b = models.TextField()
    jawaban_c = models.TextField()
    jawaban_d = models.TextField()
    poin = models.TextField()

class QuizModel(models.Model):
    level = models.IntegerField(default=1)
    quiz_xls = models.FileField(upload_to='quiz/', validators=[validate_quiz_file])

def create_quiz(sender, instance, created, **kwargs):
    try:
        quiz_entry = QuizEntryModel.objects.filter(level=instance.level)
        quiz_entry.delete()
    except QuizEntryModel.DoesNotExist:
        pass
    
    workbook = xlrd.open_workbook(instance.quiz_xls.path)
    for sheet in workbook.sheets():
        for row in range(sheet.nrows):
            QuizEntryModel.objects.create(
                level = sheet.cell(row, 0).value,
                nomor = sheet.cell(row, 1).value,
                soal = sheet.cell(row, 2).value,
                jawaban_a = sheet.cell(row, 3).value,
                jawaban_b = sheet.cell(row, 4).value,
                jawaban_c = sheet.cell(row, 5).value,
                jawaban_d = sheet.cell(row, 6).value,
                poin = sheet.cell(row, 7).value
            )

def delete_quiz(sender, instance, *args, **kwargs):
    try:
        level = QuizEntryModel.objects.filter(level=instance.level)
        level.delete()
    except UserQuizEntryModel.DoesNotExist:
        pass

signals.post_save.connect(receiver=create_quiz, sender=QuizModel)
signals.post_delete.connect(receiver=delete_quiz, sender=QuizModel)