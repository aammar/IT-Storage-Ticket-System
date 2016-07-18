from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *

# Create your views here.
def index(req):
  items = Item.objects.all()
  D = dict()
  for i in items:
    try:
      D[i.category] += [i]
    except:
      D[i.category] = [i]
  items = []
  for k in D.keys():
    items += [[str(k), D[k]]]
  return render(req, 'index.html', {"items": items})

def adminindex(req):
  return HttpResponse("HI")

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

