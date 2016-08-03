from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from models import *

# Create your views here.
def index(req):
  if req.user.is_authenticated():
    return HttpResponseRedirect(reverse('adminview'))

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
  if not req.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))

  return render(req, 'admin.html')

def employeeview(req):
  if not req.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))

  employees = Owner.objects.all()
  return render(req, 'employees.html', {"employees": employees, "active_employees": "active"})

def reqview(req):
  if not req.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))

  requests = ItemRequest.objects.all()
  return render(req, 'reqview.html', {"requests": requests, "active_requests": "active"})

def inventoryview(req):
  if not req.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))

  items = Item.objects.filter(owner=None)
  D = dict()
  for i in items:
    try:
      it = D[str(i)]
      D[str(i)] = [it[0], it[1] + 1]
    except:
      D[str(i)] = [i, 1]
  items = []
  for k in D.keys():
    items += [[D[k][0], D[k][1]]]
  return render(req, 'inventory.html', {"items": items, "active_inventory": "active"})

def user(req, userid):
  if not req.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))

  try:
    user = Owner.objects.get(user__id=userid)
  except:
    return HttpResponseRedirect(reverse('index'))
  return render(req, 'user.html', {"user": user})
