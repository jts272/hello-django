from django.shortcuts import render, redirect, get_object_or_404
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


"""The item_id is passed in, which is the href given on the Edit button.
Django creates the item.id, which itself is an iteration we created in
the template for loop.

item_id is used in urls.py with angled bracket syntax.
"""


def edit_item(request, item_id):
    # Get item from the db
    # The item id equals that passed into the view via the url
    item = get_object_or_404(Item, id=item_id)
    # Prefill with the item we just got from the db
    form = ItemForm(instance=item)
    context = {
        'form': form
    }

    if request.method == "POST":
        # Provide the specific item instance to update
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    return render(request, 'todo/edit_item.html', context)
