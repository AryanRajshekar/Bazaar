from django.db import models
from item.models import Item
from django.contrib.auth.models import User
# Create your models here.
class Conversation(models.Model):
    # using related names of reverse relationship
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name = 'conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        # query is arranged in descending order
        # 'modified_at for ascending order
        ordering= ('-modified_at',)

class ConversationMessage(models.Model):
    # in a Foreignkey models can be invoked of the related class
    conversation = models.ForeignKey(Conversation, related_name = 'messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name = 'created_messages', on_delete=models.CASCADE)
