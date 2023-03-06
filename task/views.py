from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import TaskForm
from .models import Task
from django.contrib import messages


class Index(View):
    template_name = 'task/index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.context = {
            'tasks': Task.objects.all().order_by('-id'),
            'taskform': TaskForm(),
        }

        self.render = render(self.request, self.template_name, self.context)

    def get(self, *args, **kwargs):
        return self.render


class Create(View):
    template_name = 'task/index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.render = render(self.request, self.template_name)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        task = self.request.POST.get('task')
        task_db = Task.objects.filter(task=task)

        if task_db:
            messages.error(self.request,
                           'Você já tem uma task criada com esse nome!')
            return redirect('task:index')

        Task.objects.create(task=task)

        return redirect('task:index')


class DeleteTask(View):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')

        Task.objects.filter(pk=pk).delete()

        messages.success(self.request,
                         'Task deletada')
        return redirect('task:index')


class Finished(View):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)

        if task.status == 'F':
            print('Já está como finalizado')
            return redirect('task:index')

        task.status = 'F'
        task.save()

        return redirect('task:index')
