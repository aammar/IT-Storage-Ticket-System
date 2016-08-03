from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from models import *

# Create your views here.
def index(req):
  items = Item.objects.filter(owner=None)
  D = dict()
  for i in items:
    try:
      exists = False
      for ditem in D[i.category]:
        if str(ditem) == str(i):
          exists = True
      if not exists:
        D[i.category] += [i]
    except:
      D[i.category] = [i]
  items = []
  for k in D.keys():
    items += [[str(k), D[k]]]
  return render(req, 'index.html', {"items": items})

def adminindex(req):
  return HttpResponse("HI")

def adminindex(req):
  return render(req, 'admin.html')

def employeeview(req):
  return render(req, 'employees.html')

def reqview(req):
  requests = ItemRequest.objects.all()
  return render(req, 'reqview.html', {"requests": requests})

def user(req, userid):
  try:
    user = Owner.objects.get(user__id=userid)
  except:
    return HttpResponseRedirect(reverse('index'))
  return render(req, 'user.html', {"user": user})
