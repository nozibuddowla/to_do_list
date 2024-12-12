from django.shortcuts import render, redirect
from .models import Task
from .forms import SearchForm, AddTodoForm
from .models import Todo

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
"""
def todos(request):
    todos = [
        {"title": "Buy groceries", "completed": False},
        {"title": "Do laundry", "completed": False},
        {"title": "Clean Balcony", "completed": True},
        {"title": "Buy milk", "completed": False},
        {"title": "Walk the dog", "completed": True},
        {"title": "Study for exam", "completed": False}
    ]

    search_form = SearchForm(request.POST)

    search_term = ""

    if search_form.is_valid():
        search_term = search_form.cleaned_data.get('query')

    searched_todo = []

    for todo in todos:
        if search_term and search_term.lower() in todo.get('title').lower():
            searched_todo.append(todo)

    context = {
        "todos": searched_todo,
        "search_form": search_form
    }

    return render(request, 'cool_todo/todos.html', context=context)
"""

def todos(request):
    todos = Todo.objects.all()
    search_form = SearchForm(request.GET or None)
    add_todo_form = AddTodoForm(request.POST or None)

    if request.method == 'POST' and add_todo_form.is_valid():
        add_todo_form.save()
        return redirect('todos')
    
    if search_form.is_valid():
        search_term = search_form.cleaned_data.get('query')
        if search_term:
            todos = todos.filter(title__icontains=search_term)
    
    context = {
        "todos": todos,
        "add_todo_form": add_todo_form,
        "search_form": search_form,
    }
    return render(request, 'cool_todo/todos.html', context=context)
