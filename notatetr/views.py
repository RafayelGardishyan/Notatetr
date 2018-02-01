from django.shortcuts import render, redirect
from . import models
# Create your views here.
from django.template import loader
from django.http import HttpResponse

# Create your tests here.
def login(request):
    if request.method == "POST":
      try:
        user = models.User.objects.get(email=request.POST['email'], password=request.POST['password'])
        request.session["notatetr_user_id"] = user.slug
        request.session["notatetr_logged_in"] = True
        return redirect("/")
      except Exception as e:
        return HttpResponse("No User: {}".format(e))
    else:
      template = loader.get_template("notebook/login-register.html")
      return HttpResponse(template.render(request=request, context={}))

def index(request):
    if request.session["notatetr_logged_in"]:
      return HttpResponse(request.session["notatetr_user_id"])
    else:
      return HttpResponse(index)