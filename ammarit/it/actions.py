from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from models import *

import json

def login_action(req):
  if not (req.method == "POST"):
    return HttpResponse('')

  try:
    password = req.POST['password']
    username = req.POST['username']
    user = authenticate(username=username, password=password)
    if user is not None and (user.is_staff or user.is_superuser):
      login(req, user)
      return HttpResponse("ok")
  except:
    return HttpResponse("Invalid username/password")
  return HttpResponse("Invalid username/password")

def logout_action(req):
  if not (req.method == "POST"):
    return HttpResponse('')
  if req.user.is_authenticated():
    logout(req)
  return HttpResponse("ok")

def makerequest(req):
  if (req.method != "POST"):
    return HttpResponse("Unknown error")
  try:
    requesterID = int(req.POST['id'])
    items = req.POST['items']
    desc = req.POST['desc']
    items = json.loads(items)
  except:
    return HttpResponse("Unknown error")

  try:
    requester = Owner.objects.get(user__id=requesterID)
  except Exception as e:
    return HttpResponse("Invalid user ID")

  r = ItemRequest(requester=requester, desc=desc)
  r.save()
  for i in items:
    ri = RequestedItem(request=r, itemNumber=int(i))
    ri.save()

  return HttpResponse("ok")

def accept_req(req):
  try:
    reqid = int(req.POST['reqid'])
    desc = req.POST['desc']
  except:
    return HttpResponse("Invalid request")

  try:
    req = RequestedItem.objects.get(id=reqid)
  except:
    return HttpResponse("Item request not found")

  try:
    item = Item.objects.filter(itemNumber=req.itemNumber, owner=None)[0]
  except:
    return HttpResponse("Out of stock")

  item.owner = req.request.requester
  item.ownership_desc = desc
  item.save()
  if RequestedItem.objects.filter(request=req.request).count() == 1:
    req.request.delete()
  req.delete()

  return HttpResponse("ok")

def reject_req(req):
  try:
    reqid = int(req.POST['reqid'])
    desc = req.POST['desc']
  except:
    return HttpResponse("Invalid request")

  try:
    req = RequestedItem.objects.get(id=reqid)
  except:
    return HttpResponse("Item request not found")

  if RequestedItem.objects.filter(request=req.request).count() == 1:
    req.request.delete()
  req.delete()

  return HttpResponse("ok")

def return_item(req):
  try:
    itid = int(req.POST['itid'])
  except:
    return HttpResponse("Invalid request")

  try:
    item = Item.objects.get(itemID=itid)
  except:
    return HttpResponse("Item not found")

  item.owner = None
  item.save()

  return HttpResponse("ok")

def lost_item(req):
  try:
    itid = int(req.POST['itid'])
  except:
    return HttpResponse("Invalid request")

  try:
    item = Item.objects.get(itemID=itid)
  except:
    return HttpResponse("Item not found")

  item.delete()

  return HttpResponse("ok")

def delete_user(req):
  try:
    uid = int(req.POST['uid'])
  except:
    return HttpResponse("Invalid request")

  try:
    usr = User.objects.get(id=uid)
  except:
    return HttpResponse("User not found")

  usr.delete()

  return HttpResponse("ok")

def addnewitem(req):
  try:
    id = int(req.GET['itemid'])
    make = req.GET['itemmake']
    model = req.GET['itemmodel']
    number = int(req.GET['itemnumber'])
    url = req.GET['itemurl']
    desc = req.GET['itemdesc']
    category = req.GET['itemcat']
  except:
    return HttpResponse("Invalid Request")

  try:
    it = Item(itemID=id, make=make, model=model, description=desc, imgURL=url, itemNumber=number, category=category)
    it.save()
  except:
    return HttpResponse("Cannot create item")

  return HttpResponse("ok")

def restockitem(req):
  try:
    id = int(req.GET['itemid'])
    number = int(req.GET['itemnumber'])
  except:
    return HttpResponse("Invalid Request")

  try:
    existing = Item.objects.filter(itemNumber=number)[0]
    it = Item(itemID=id, make=existing.make, model=existing.model, description=existing.description, imgURL=existing.imgURL, itemNumber=number, category=existing.category)
    it.save()
  except:
    return HttpResponse("Cannot create item")

  return HttpResponse("ok")
