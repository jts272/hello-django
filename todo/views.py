from django.shortcuts import render
# Get access to the Item model
from .models import Item

# Create your views here.


def get_todo_list(request):
    # Get django queryset
    items = Item.objects.all()
    context = {
        'items': items
    }
    # return an http response by taking a request and template name
    # Give access to context var
    return render(request, 'todo/todo_list.html', context)
