from food_app.models import Person_food,Favaorites
from django.contrib.auth.models import User
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

