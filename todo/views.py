from django.shortcuts import render, redirect
# Get access to the Item model
from .models import Item
# For form created using Django
from .forms import ItemForm

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


def add_item(request):
    if request.method == "POST":
        # DJANGO POST HANDLER
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

        # MANUAL POST HANDLER - error when using Django form
        # name = request.POST.get('item_name')
        # # For bool, check if this property exists in the post object
        # is_done = 'is_done' in request.POST
        # # Use these vars to create an item for the table
        # Item.objects.create(
        #     name=name,
        #     is_done=is_done
        # )
        # Then redirect on POST
        # return redirect('get_todo_list')

    # Create instance of form made by Django in forms.py
    form = ItemForm()
    # Create context to pass to the render function
    context = {
        'form': form
    }

    # return an http response by taking a request and template name
    # Give access to context var
    return render(request, 'todo/add_item.html', context)
