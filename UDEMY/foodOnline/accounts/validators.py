from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
    ext=os.path.splitext(value.name)[1]
    print(ext)
    valid_extensions=['.png','.jpg','.jpeg']
    if not ext.lower() is valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions: '+ str(valid_extensions))