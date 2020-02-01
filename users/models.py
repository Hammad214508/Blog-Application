from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'

    # Causes problems with AWS so I commented out
    # Will have to use lambda functions 

    # # it runs after model is saved, we are overriding
    # # Need *args, **kwargs as needed for the parent class
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs) #Run the save for the parent class
    #     # Grab the image and resize it
    #     img = Image.open(self.image.path)
    #     if img.width > 300 or img.height > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
