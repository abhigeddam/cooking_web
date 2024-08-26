from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import requests
import json
from food_app.models import Cusines,Diet,Intolerences,Person_food,Reciepes,Trending
from database.models import Profile
from .functions import historyChange,trendChange
from django.contrib.auth.models import User
from food_app.form import *
# Create your views here.

def api_post(request):
    if request.method == 'GET':
        search = request.GET.get('query')
        Cusine = request.GET.get('Cusine')
        Diets = request.GET.get('Diet')
        Avoid = request.GET.get('avoid')
        data = Reciepes.objects.all().filter(name__contains=search)
        if len(data) > 0:
            return render(request, 'search.html',{'response':data,'i':0})
        else:
            payload = {'apiKey':"",'query':search,'cuisine':Cusine,'diet':Diets,'intolerances':Avoid}
            response = requests.get('https://api.spoonacular.com/recipes/complexSearch',payload)
            response = response.json()
            return render(request, 'search.html',{'response':response['results'],'i':1})
@login_required(login_url='logins')
def api_search(request):
    form = receipe_Form()
    x = Cusines.objects.all()
    y = Diet.objects.all()
    a = Intolerences.objects.all()
    z = request.session.get('id','')
    user = User.objects.get(id=z)
    Reciepes_shared = len(user.recipes.all())
    profile = Profile.objects.get(user=user)
    following = len(profile.following.all())
    followers = len(user.followers.all())
    data = Person_food.objects.filter(user_id=user).first()
    trending = Trending.objects.all()
    trending = Trending.objects.all()[:3]
    if data != None:
        r1,r2,r3 = data.last_reciepe1.split('??'),data.last_reciepe2.split('??'),data.last_reciepe3.split('??')
    else:
        r1,r2,r3 = [' ',' '],[' ',' '],[' ',' ']
    print(r1,r2,r3)
    if request.method == "POST":
        print(request.POST)
        query = request.POST['search']
        Cusine = request.POST['Cusines']
        Diets = request.POST['Diet']
        avoid = request.POST['Avoid']
        return HttpResponseRedirect('/api/list/?query={q}&Cusine={c}&Diet={d}&avoid={a}'.format(q=query, c=Cusine,d = Diets,a=avoid))
    return render(request,'main.html',{'x':x,'y':y,'a':a,'z':z,'n1':r1[0],'n2':r2[0],'n3':r3[0],'i1':r1[1],'i2':r2[1],'i3':r3[1],'form':form,'Trending':trending,'Profile':profile,'Recipes':Reciepes_shared,'following':following,'followers':followers})
@login_required(login_url='logins')
def api_display(request):
    if request.method == "GET":
        y = request.session.get('id','')
        user = Profile.objects.get(user__id=y)
        if user.searches_left <= 0:
            return redirect('Shop')

        else:
            user.searches_left -= 1
            user.save()

        data = request.GET
        id = data.get('id')
        image = data.get('image')
        name = data.get('name')
        ans = data.get('ans')
        payload = {'apiKey':"149a99cd6a4c423886643debcbdec074"}
        url = 'https://api.spoonacular.com/recipes/'
        url = url + id + '/analyzedInstructions'
        response = requests.get(url,payload).json()
        urls = 'https://youtube.googleapis.com/youtube/v3/search'
        payloads = {'regionCode':'us','q':name+" recipe",'key':''}
        send = requests.get(urls,payloads).json()
        send = send['items'][0]['id']['videoId']
        send = 'https://www.youtube.com/embed/' + send
        print(send)
        historyChange(request,name,image)
        trendChange(request,id,name,image)



    return render(request,'display.html',{'name':name,'steps':response[0]['steps'],'image':image,'video':send,'id':id})
def account(request):
    if request.method == 'POST':
        a = {'name':request.POST['name'],'steps':request.POST['steps'],'user_id':User.objects.get(username=request.session.get('user',0))}
        form = Main_receipe_Form(a, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = receipe_Form()
        return render(request,'account.html',{'form':form})

@login_required(login_url='logins')
def api_display_internal(request):
    if request.method == "GET":
        data = request.GET
        ids = data.get('id')
        image = data.get('image')
        name = data.get('name')
        x = Reciepes.objects.all().filter(id=ids).first()
        steps = x.steps
        urls = 'https://youtube.googleapis.com/youtube/v3/search'
        payloads = {'regionCode':'us','q':name,'key':'AIzaSyAwCqp0AE43pxZnyOPjmcE70QJp-92Yli8'}
        send = requests.get(urls,payloads).json()
        send = send['items'][0]['id']['videoId']
        send = 'https://www.youtube.com/embed/' + send
        num = len(steps)
        return render(request,'display_internal.html',{'name':name,'steps':steps,'image':image,'video':send,'id':ids,'num':num})


