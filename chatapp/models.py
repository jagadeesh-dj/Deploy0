from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name="receiver")
    message=models.TextField()
    clear_by_sender=models.BooleanField(default=False)
    clear_by_receiver=models.BooleanField(default=False)
    is_read=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.receiver}'
    


class UserStatus(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_status')
    status=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    