from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm
# Create your views here.

@login_required
def new_conversation(request,item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    # filters where the got item in this function is the same item being called
    conversations = Conversation.objects.filter(item=item).filter(members__in =[request.user.id] )

    if conversations:
        return redirect('message:detail', pk=conversations.first().id)

    if request.method=='POST':
        form= ConversationMessageForm(request.POST)

        if form.is_valid():
            #saving all form info to database
            # .create saves your info in the database directly
            # creates a convo instance with the item specified
            conversation = Conversation.objects.create(item=item)
            # adding the user who wants to contact to db
            conversation.members.add(request.user)
            # adding the user who created the item
            conversation.members.add(item.created_by)
            # form is saved in convo_message
            conversation_message = form.save(commit=False)
            # set the convo_message and conversation attribute to the above convo variable
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html',{
        'form': form
    })

