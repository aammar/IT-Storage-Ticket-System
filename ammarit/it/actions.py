from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from models import *

import json

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

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

  logstr = "<a href='"+reverse("user", args=(str(requester.user.id),))+"'>"+str(requester)+"</a> ["+get_client_ip(req)+"] requested " + str(len(items)) + " item(s)"
  subtext = "<p>Request description: " + desc + "</p>"
  subtext += "<p> Requested items: "
  for i in items:
    subtext += "<span class='label label-default'>" + str(i) + "</span> "
  subtext += "</p>"
  l = Log(logText=logstr, type="warning", subtext=subtext)
  l.save()

  r = ItemRequest(requester=requester, desc=desc)
  r.save()
  for i in items:
    ri = RequestedItem(request=r, itemNumber=int(i))
    ri.save()

  return HttpResponse("ok")

def accept_req(request):
  try:
    reqid = int(request.POST['reqid'])
    desc = request.POST['desc']
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

  logstr = str(request.user.username)+" accepted " + "<a href='"+reverse("user", args=(str(req.request.requester.user.id),))+"'>"+str(req.request.requester)+"</a>'s request of a " + str(item) + " <span class='label label-default'>"+str(item.itemNumber)+"</span>"
  subtext = "Response: " + desc
  l = Log(logText=logstr, type="success", subtext=subtext)
  l.save()

  item.owner = req.request.requester
  item.ownership_desc = desc
  item.save()
  if RequestedItem.objects.filter(request=req.request).count() == 1:
    req.request.delete()
  req.delete()

  return HttpResponse("ok")

def reject_req(request):
  try:
    reqid = int(request.POST['reqid'])
    desc = request.POST['desc']
  except:
    return HttpResponse("Invalid request")

  try:
    req = RequestedItem.objects.get(id=reqid)
  except:
    return HttpResponse("Item request not found")

  try:
    item = Item.objects.filter(itemNumber=req.itemNumber, owner=None)[0]
  except:
    item = None

  logstr = str(request.user.username)+" rejected " + "<a href='"+reverse("user", args=(str(req.request.requester.user.id),))+"'>"+str(req.request.requester)+"</a>'s request of a " + str(item) + " <span class='label label-default'>"+str(item.itemNumber)+"</span>"
  subtext = "Response: " + desc
  l = Log(logText=logstr, type="danger", subtext=subtext)
  l.save()

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

  logstr = str(req.user.username)+" returned item " + str(item) + "<span class='label label-default'>"+str(item.itemNumber)+"</span> from <a href='"+reverse("user", args=(str(item.owner.user.id),))+"'>" + str(item.owner) + "</a>"
  subtext = ""
  l = Log(logText=logstr, type="info", subtext=subtext)
  l.save()

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

  logstr = str(req.user.username)+" marked item " + str(item) + "<span class='label label-default'>"+str(item.itemNumber)+"</span> from <a href='"+reverse("user", args=(str(item.owner.user.id),))+"'>" + str(item.owner) + "</a> as lost"
  subtext = ""
  l = Log(logText=logstr, type="info", subtext=subtext)
  l.save()

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
