from food_app.models import Person_food,Favaorites,Trend_container,Trending
from django.contrib.auth.models import User
import datetime
def historyChange(request,name,img):
        user = User.objects.get(username=request.session.get('user',0))
        data = Person_food.objects.filter(user_id=user).first()
        if data == None:
            data = Person_food(user_id=user,last_reciepe1='/??/',last_reciepe2='/??/',last_reciepe3='/??/')
            data.save()
        l = name+'??'+img
        if not (l == data.last_reciepe1 or l == data.last_reciepe2 or l == data.last_reciepe3):
            x = data.last_reciepe2
            data.last_reciepe2 = data.last_reciepe1
            data.last_reciepe3 = x
            data.last_reciepe1 = l
            data.save()



def trendChange(request,id,name,image):
    x = Trend_container.objects.filter(ids=id)
    if len(x) == 0:
        y  = Trend_container(ids=id,item=name,image=image)
        y.save()
    if len(x) == 1:
        x.first().views += 1
    if (Trending.objects.all().first().time.hour < datetime.datetime.now().hour or Trending.objects.all().first().time.minute < datetime.datetime.now().minute ) and len(Trend_container.objects.all())>=3:
        x = Trend_container.objects.all().order_by('views')
        Trending.objects.all().delete()
        for hm in range(3):
            Trending(ids=x[hm].ids,item=x[hm].item,image=x[hm].image).save()
        x.delete()
            






    

