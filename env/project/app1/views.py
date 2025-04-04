from django.shortcuts import render,HttpResponse,redirect,get_object_or_404

from .models import Read
from .forms import Add
# Create your views here.


def Home(req):
    return render(req,"index.html")

def About(req):
    return render(req,'about.html')

def Readme(req):
    read=Read.objects.all()
    context={
        'read': read
    }
    return render(req,'read.html',context)

def Add_some(req):
    if req.method=="POST":
        form=Add(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("added")
    else:
        form=Add()
        return render(req,'add.html',{'form':form})
 

def Edit(req):
    user_id=req.GET.get("id")
    user=Read.objects.get(id=user_id)
    if req.method=="POST":
        form=Add(req.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect("read_data")
        
    else:
        form=Add(instance=user)
    return render(req,'edit.html',{'form':form})    



def Delete(req):
    user_id = req.GET.get("id")
    user = get_object_or_404(Read, id=user_id)
    user.delete()
    return redirect("read_data")
