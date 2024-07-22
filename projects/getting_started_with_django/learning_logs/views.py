from django.shortcuts import render
from .models import Topic


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

