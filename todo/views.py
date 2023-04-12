from django.shortcuts import render

# Create your views here.


def get_todo_list(request):
    # return an http response by taking a request and template name
    return render(request, 'todo/todo_list.html')
