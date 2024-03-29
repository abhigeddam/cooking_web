from django.shortcuts import render,redirect
from food_app.models import Person_food,Favaorites,Reciepes
from django.contrib.auth.models import User
from .models import Profile
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


def Account(request):
    data = request.GET
    username = data.get('username')
    number = int(data.get('number'))
    user = User.objects.get(username=username)
    data = Reciepes.objects.filter(user_id=user)
    data = data[number*6:min((number+1)*6,len(data))]
    print(data[0].description,'hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    return render(request,'Account.html',{'data':data,'number':number})



    
def Deletefav(request):
    data = request.GET
    ids = data.get('id')
    user = User.objects.get(username=request.session.get('user',0))
    x = Favaorites.objects.filter(user_id=user,ids=ids).first()
    x.delete()

def Community(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        searches = Profile.objects.filter(user__username__contains=name)
        print(searches)
        return render(request,'profile_search.html',{'Searches':searches})

    y = request.session.get('id','')
    z = request.GET.get('num',0)
    user = Profile.objects.get(user__id=y)
    data = []
    for hm in user.following.all():
        if len(hm.recipes.all()) > z:
            data.append([hm.recipes.all()[z],hm.username,hm.Profile.image])
    return render(request,'community.html',{'data':data,})
    

def addfollowers(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        x = User.objects.filter(id = ids).first()
        y = request.session.get('id','')
        z = Profile.objects.get(user__id=y)
        z.following.add(x)
        return redirect('community')



def Recipe_submission(request):
    if request.method == 'POST':
        steps = request.POST.get('steps')
        steps = list(steps.split('.'))
        a = {'name':request.POST['name'],'description':request.POST['description'],'steps':steps,'user_id':User.objects.get(username=request.session.get('user',0))}
        form = Main_receipe_Form(a, request.FILES)
        if form.is_valid():
            form.save()
            y = request.session.get('id','')
            user = Profile.objects.get(user__id=y)
            user.coins += 100
            user.save()
            return redirect('api_searchs')
    else:
        form = receipe_Form()
        return render(request,'account.html',{'form':form})



def Shop(request):
    y = request.session.get('id','')
    user = Profile.objects.get(user__id=y)
    data = {'coins': user.coins,'searches': user.searches_left}
    return render(request,'shop.html',data)