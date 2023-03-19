from django.shortcuts import render,redirect
from food_app.models import Person_food,Favaorites
from django.contrib.auth.models import User
from food_app.form import *
# Create your views here.
def Favmanager(request):
    if request.method == "GET":
        data = request.GET
        ids = data.get('id')
        name = data.get('name')
        image = data.get('img')
        user = User.objects.get(username=request.session.get('user',0))
        print(user)
        x = Favaorites(name=name,image=image,ids=ids,user_id=user)
        x.save()
    if request.method == "POST":
        data = request.POST
        ids = data.get('id')
        print(ids,'hii')
        user = User.objects.get(username=request.session.get('user',0))
        x = Favaorites.objects.filter(user_id=user,ids=ids).first()
        x.delete()
        return redirect('Fav')

def Favdisp(request):
     user = User.objects.get(username=request.session.get('user',0))
     data = Favaorites.objects.filter(user_id=user)
     print(data)
     return render(request,'Fav.html',{'data':data ,'length':len(data)})


def account(request):
    if request.method == 'POST':
        a = {'name':request.POST['name'],'steps':request.POST['steps'],'user_id':User.objects.get(username=request.session.get('user',0))}
        form = Main_receipe_Form(a, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('api_searchs')
    else:
        form = receipe_Form()
        return render(request,'account.html',{'form':form})

    
def deletefav(request):
    data = request.GET
    ids = data.get('id')
    user = User.objects.get(username=request.session.get('user',0))
    x = Favaorites.objects.filter(user_id=user,ids=ids).first()
    x.delete()
    return redirect('Fav')
    

    


