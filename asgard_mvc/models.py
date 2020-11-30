from django.db import models

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.username, filename)

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', 'jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

# Create your models here.
class UserProfileModel(models.Model):
    username = models.CharField(max_length=100)
    image_profile = models.ImageField(upload_to=user_directory_path, validators=[validate_file_extension])