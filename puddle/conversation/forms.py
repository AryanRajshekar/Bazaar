from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        # model references the model in models.py you want to reference
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content' : forms.Textarea(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border'
            })
        }
