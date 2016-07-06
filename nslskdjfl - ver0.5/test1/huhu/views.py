from django.shortcuts import render
from .models import Seperate
from .models import Dice
from .models import PlayerPosition
from .models import Order
import random

# Create your views here.

def index(request):
	seperate = Seperate.objects.all()
	dice = Dice.objects.all().last()
	playerP = PlayerPosition.objects.all().last()
	orders = Order.objects.all().last()
	return render(request,'main/index.html', {'seperate':seperate,'dice':dice,'playerP':playerP,'orders':orders})

def insert(request):
	road = []
	for i in range(0,150):
		road.append(0)
	mineCount = 0
	count = 0

	while mineCount != 10:
		mine = random.randrange(0, 100)
		if road[mine]==0:
			road[mine] = 1
			mineCount = mineCount + 1

	for a in range(0, 150):
		seperate = Seperate()
		if road[a]==0:
			seperate.seperMine = 0
			seperate.save()
		elif road[a]==1:
			seperate.seperMine = 1
			seperate.save()

	playerp = PlayerPosition()
	playerp.player1Position = 0
	playerp.player2Position = 0
	playerp.save()
	orders = Order()
	orders.order = 1
	orders.save()
	return render(request, 'main/insert.html', {})

def passnext(request):
	dice = Dice()
	dices1 = random.randrange(1, 7)
	dices2 = random.randrange(1, 7)
	dice.dice1 = dices1
	dice.dice2 = dices2
	dice.save()

#	playerp = PlayerPosition()
#	playerp.player1Position = dice.dice1+dice.dice2
#	playerp.player2Position = 0
#	playerp.save()
	orders = Order.objects.all().last()
	orderc = Order()
	if orders.order == 1:
		position = PlayerPosition.objects.all().last()
		position.player1Position = position.player1Position + dice.dice1 + dice.dice2
		#지뢰 확인 조건반복문 하기
		orderc.order = 0
		if dice.dice1 == dice.dice2 :
			orderc.order =1
		if position.player1Position >=100:
			orderc.order =2
		position.save()
		orderc.save()

	elif orders.order ==0:
		position = PlayerPosition.objects.all().last()
		position.player2Position = position.player2Position + dice.dice1 + dice.dice2
		orderc.order = 1
		if dice.dice1 == dice.dice2 :
			orderc.order =0
		if position.player2Position >=100:
			orderc.order =2
		position.save()
		orderc.save()
	return render(request, 'main/passnext.html', {})