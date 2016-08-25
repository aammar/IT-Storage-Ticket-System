from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from it.models import *

admin.site.register(Owner)
admin.site.register(Item)
admin.site.register(ItemRequest)
admin.site.register(RequestedItem)
admin.site.register(Log)
