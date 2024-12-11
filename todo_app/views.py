from django.shortcuts import render
from .models import Task
from .forms import SearchForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    completed = request.GET.get('completed')
    if completed == '1':
        tasks = tasks.filter(completed = True)
    elif completed == '0':
        tasks = tasks.filter(completed = False)
    return render(request, 'task_list.html', {'tasks': tasks})

def task_details(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def todos(request):
    todos = [
        {"title": "Buy groceries", "completed": False},
        {"title": "Do laundry", "completed": False},
        {"title": "Clean Balcony", "completed": True},
        {"title": "Buy milk", "completed": False},
        {"title": "Walk the dog", "completed": True},
        {"title": "Study for exam", "completed": False}
    ]

    search_form = SearchForm()

    data = request.GET
    search_term = data.get('query', '')

    searched_todo = []
    for todo in todos:
        if search_term.lower() in todo.get('title').lower():
            searched_todo.append(todo)

    context = {
        "todos": searched_todo,
        "search_form": search_form
    }

    return render(request, 'cool_todo/todos.html', context=context)
