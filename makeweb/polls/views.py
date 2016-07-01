from django.shortcuts import render
from .models import Register
from .models import Board
# Create your views here.

def index(request):
	return render(request, 'main/index.html', {})

def login(request):
	return render(request, 'main/login.html', {})

def register(request):
	return render(request, 'main/register.html', {})

def registeraction(request):
	user_id = request.POST["register_id"]
	user_pw = request.POST["register_pw"]
	#user_agpw = request.POST["register_agpw"]
	#if user_pw == user_agpw:
	register = Register()
	register.username = user_id
	register.password = user_pw
	register.save()
	return render(request, 'main/registeraction.html', {})
	#else:
	#	def registererror(request):
	#		return render(request, 'main/registererror.html', {})

def loginaction(request):
	user = request.GET["login_id"]
	passwd = request.GET["login_pw"]
	try:
		if(user == "qudgh7145"):
			a = Register.objects.get(username=user)
			if a.password == passwd:
				request.session['pppp'] = a.username
				return render(request, 'main/loginaction.html', {})		

		m = Register.objects.get(username=user)

		if m.password == passwd:
			request.session['usid'] = m.username
			return render(request, 'main/loginaction.html', {})		
	except Exception, e:
		pass
	return render(request, 'main/index.html', {})
		
def logout(request):
	request.session.flush()
	return render(request, 'main/logout.html', {})

def about(request):
	board = Board.objects.all()
	return render(request, 'main/about.html', {'board': board})

def insert(request):
	return render(request, 'main/insert.html', {})

def insertaction(request):
	insert_title = request.POST["insert_title"]
	insert_content = request.POST["insert_content"]
	insert_writer = request.POST["insert_writer"]
	board = Board()
	board.subject = insert_title
	board.contents = insert_content
	board.writer = insert_writer
	board.save()
	return render(request, 'main/insertaction.html', {})

def view(request):
	num = request.GET["id"]
	board = Board.objects.get(id=num)
	return render(request, 'main/view.html', {'board': board})
