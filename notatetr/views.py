from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse

# Create your tests here.
def login(request):
    if request.method == "POST":
      pass
    else:
      template = loader.get_template("notebook/login-register.html")
      return HttpResponse(template.render(request=request, context={}))