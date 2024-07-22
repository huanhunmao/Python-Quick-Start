from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


def topics_detail(request, topic_id):
    """Show a single topic and all its entries."""
    try:
        topic = Topic.objects.get(id=topic_id)
        entries = topic.entry_set.order_by('-date_added')
        context = {'topic': topic, 'entries': entries}
        return render(request, 'topics_detail.html', context)
    except Topic.DoesNotExist:
        return render(request, 'not_found.html')


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
         form = TopicForm()
    else:
        # POST data submitted; process data.
         form = TopicForm(data=request.POST)
         if form.is_valid():
             form.save()
             return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'new_topic.html', context)
