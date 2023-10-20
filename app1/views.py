from django.shortcuts import render , redirect, get_object_or_404
from .forms import Taskform
from .models import Task
from multiprocessing import context


def Home(request):
    form = Taskform()
    if request.method == "POST":
        form = Taskform(request.POST)
        form.save()
        form=Taskform()

    data=Task.objects.all()
    context = {
        'form': form,
        'data':data,
    }
    return render(request, "app1/index.html", context)



def Delete_record(request,id):
    a=Task.objects.get(pk=id)
    a.delete()
    return redirect("/")






def Update_Record(request, id):
    if request.method == "POST":
        data = get_object_or_404(Task, pk=id)  
        form = Taskform(request.POST, instance=data)
        if form.is_valid():
            form.save()
    else:
        data = get_object_or_404(Task, pk=id)
        form = Taskform(instance=data)

    context = {
        'form': form,
    }

    return render(request, 'app1/update.html', context)
