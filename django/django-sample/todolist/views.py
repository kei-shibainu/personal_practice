from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context['tasks'].filter(user=self.request.user)

        searchInputText = self.request.GET.get('search') or ""
        if searchInputText:
            context["tasks"] = context['tasks'].filter(title__startswith=searchInputText)

        context["search"] = searchInputText
        return context
    

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # __all__ 全てのmodelを指定省略記法
    fields = ['title', 'description', 'completed']
    # redirect設定
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    fields = "__all__"
    success_url = reverse_lazy('tasks')

class TaskListLoginView(LoginView):
    fields = '__all__'
    template_name = 'todolist/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')

class RegisterTodoApp(FormView):
    template_name = 'todolist/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)            
        return super().form_valid(form)
    