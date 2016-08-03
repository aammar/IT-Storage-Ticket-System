from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from models import *

@csrf_exempt
def makerequest(req):
  if (req.method != "POST"):
    return HttpResponse("Unknown error")
  try:
    requesterID = int(req.POST['id'])
    requestedItemID = int(req.POST['itemid'])
    requestedItemNumber = int(req.POST['itemnumber'])
  except:
    return HttpResponse("Unknown error")

  try:
    requester = Owner.objects.get(id=requesterID)
  except Exception as e:
    return HttpResponse("Invalid user ID")

  try:
    item = Item.objects.get(itemID=requestedItemID, itemNumber=requestedItemNumber)
  except:
    return HttpResponse("Item not found")

  r = ItemRequest(requester=requester, item=item)
  r.save()
  return HttpResponse("Request sent")

@csrf_exempt
def accept_req(req):
  try:
    reqid = int(req.POST['reqid'])
  except:
    return HttpResponse("Invalid request")

  try:
    req = ItemRequest.objects.get(id=reqid)
  except:
    return HttpResponse("Item request not found")

  req.item.owner = req.requester
  req.item.save()
  req.delete()

  return HttpResponse("ok")

@csrf_exempt
def reject_req(req):
  try:
    reqid = int(req.POST['reqid'])
  except:
    return HttpResponse("Invalid request")

  try:
    req = ItemRequest.objects.get(id=reqid)
  except:
    return HttpResponse("Item request not found")

  req.delete()

  return HttpResponse("ok")
