from django.shortcuts import render, redirect
from . import models
# Create your views here.
from django.http import HttpResponse

# Create your tests here.
def login(request):
    try:
        if request.session["notatetr_logged_in"]:
            return redirect('/')
    except Exception as e:
        return render(request, "notebook/login-register.html", {})
    if request.method == "POST":
        try:
            user = models.User.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session["notatetr_user_id"] = user.slug
            request.session["notatetr_logged_in"] = True
            return redirect("/")
        except Exception as e:
            return render(request, "notebook/login-register.html", {'error': 'Սխալ Էլ․ փոստ կամ գաղտնաբառ'})
    else:
      return render(request, "notebook/login-register.html", {})

def index(request):
    try:
        if request.session["notatetr_logged_in"]:
            return redirect('/{}/notes'.format(request.session["notatetr_user_id"]))
        else:
            return render(request, 'notebook/index.html')
    except:
        return render(request, 'notebook/index.html')

def register(request):
    if request.method == "POST":
        try:
            u = models.User()
            u.email = request.POST['email']
            u.password = request.POST['password']
            u.save()
            request.session["notatetr_user_id"] = u.slug
            request.session["notatetr_logged_in"] = True
            return redirect('/')
        except:
            return HttpResponse('Error')
    else:
        return redirect('/login')

def logged_user_home(request, id):
    if not request.session["notatetr_logged_in"]:
        return redirect('/login')
    u = models.User.objects.get(slug=int(id))
    notes = models.Note.objects.filter(user=u)
    return render(request, 'notebook/user_homepage.html', {'user': u, 'notes': notes})

def logout(request):
    request.session["notatetr_user_id"] = ""
    request.session["notatetr_logged_in"] = False
    return redirect('/')

def add(request):
    if not request.session["notatetr_logged_in"]:
        return redirect('/login')
    if request.method != 'POST':
        return render(request, 'notebook/add.html')
    else:
        u = models.User.objects.get(slug=request.session['notatetr_user_id'])
        n = models.Note()
        n.content = request.POST['content']
        n.user = u
        n.save()
        return redirect('/')
