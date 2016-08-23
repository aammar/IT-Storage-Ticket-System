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
        if ditem.sameAs(i):
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

  num_reqs = ItemRequest.objects.count()
  return render(req, 'admin.html', {"num_requests": num_reqs})

def employeeview(req):
  if not req.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))

  employees = Owner.objects.all()
  num_reqs = ItemRequest.objects.count()
  return render(req, 'employees.html', {"employees": employees, "active_employees": "active", "num_requests": num_reqs})

def reqview(req):
  if not req.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))

  requests = ItemRequest.objects.all()
  num_reqs = ItemRequest.objects.count()
  requests = map(lambda r: [r, map(lambda ri: [ri.getitem(), ri], RequestedItem.objects.filter(request=r))], requests)
  return render(req, 'reqview.html', {"requests": requests, "active_requests": "active", "num_requests": num_reqs})

def inventoryview(req):
  if not req.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))

  # make a dictionary D that maps from [item name] -> [quantity]
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

  # items is now a list of all [item, count]
  # convert to a dictionary D that maps from [category] -> [[item, count]]
  D = dict()
  for it in items:
    i = it[0]
    try:
      D[i.category] += [it]
    except:
      D[i.category] = [it]

  # finally create a list of all [category, [item, count]]
  items = []
  for k in D.keys():
    items += [[str(k), D[k]]]

  num_reqs = ItemRequest.objects.count()
  return render(req, 'inventory.html', {"items": items, "active_inventory": "active", "num_requests": num_reqs})

def additemview(req):
  requests = ItemRequest.objects.all()
  num_reqs = ItemRequest.objects.count()
  return render(req, 'additem.html', {"requests": requests, "active_additem": "active", "num_requests": num_reqs})

def user(req, userid):
  if not req.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))

  try:
    user = Owner.objects.get(user__id=userid)
  except:
    return HttpResponseRedirect(reverse('index'))

  items = Item.objects.filter(owner=user)
  print(items)
  D = dict()
  for i in items:
    try:
      it = D[str(i.itemNumber)+"-"+i.ownership_desc]
      D[str(i.itemNumber)+"-"+i.ownership_desc] = [it[0], it[1] + 1]
    except:
      D[str(i.itemNumber)+"-"+i.ownership_desc] = [i, 1]
  items = []
  for k in D.keys():
    items += [[D[k][0], D[k][1]]]

  num_reqs = ItemRequest.objects.count()
  return render(req, 'user.html', {"items": items, "user": user, "num_requests": num_reqs})
