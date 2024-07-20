from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='editing')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)