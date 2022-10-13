from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todoform
from.models import Task

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView
# Create your class based views here.
class listview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class detailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'tas'

class updateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

# Create your function based views here.
def task(request):
    ta = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':ta})

# def detail(request):
#     task=Task.objects.all()
#     return render(request,'detail.html',{'task':task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    fo=todoform(request.POST or None,instance=task)
    if fo.is_valid():
        fo.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'fo':fo})
