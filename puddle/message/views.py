from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from conversation.views import Conversation, ConversationMessageForm
# Create your views here.
@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in =[request.user.id])
    return render(request, 'message/inbox.html',{
        'conversations' : conversations
    })

@login_required
def detail(request,pk):
    conversation = Conversation.objects.filter(members__in =[request.user.id]).get(pk=pk)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('message:detail',pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'message/detail.html',{
          'conversation' : conversation,
          'form': form
     })